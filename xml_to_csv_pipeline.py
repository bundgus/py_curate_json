import xml.etree.ElementTree as ET
from xmljson import yahoo as jencoder
from py_curate_json import curate_json_core as cjc
from py_curate_json.flatten_denorm_json import flatten_denorm_json
import json
import csv


def fixup_element_prefixes(elem, uri_map, memo):
    def fixup(name):
        try:
            return memo[name]
        except KeyError:
            if name[0] != "{":
                return
            uri, tag = name[1:].split("}")
            if uri in uri_map:
                new_name = uri_map[uri] + ":" + tag
                memo[name] = new_name
                return new_name
    # fix element name
    name = fixup(elem.tag)
    if name:
        elem.tag = name
    # fix attribute names
    for key, value in elem.items():
        name = fixup(key)
        if name:
            elem.set(name, value)
            del elem.attrib[key]


def set_prefixes(elem, prefix_map):

    # check if this is a tree wrapper
    if not ET.iselement(elem):
        elem = elem.getroot()

    # build uri map and add to root element
    uri_map = {}
    for prefix, uri in prefix_map.items():
        uri_map[uri] = prefix
        elem.set("xmlns:" + prefix, uri)

    # fixup all elements in the tree
    memo = {}
    for elem in elem.getiterator():
        fixup_element_prefixes(elem, uri_map, memo)


def xml_to_json(xml_string):

    #xml_data = ET.parse('sample_json/EUOZJB.xml').getroot()
    root = ET.fromstring(xml_string)

    ns = {'asds4_0': 'http://services.sabre.com/res/asds/v4_0',
          'stl15': 'http://webservices.sabre.com/pnrbuilder/v1_15',
          'ns18': 'http://services.sabre.com/res/or/v1_8'}
    set_prefixes(root, ns)

    # Convert to JSON
    return jencoder.data(root)


# xml file with one complete xml record per line
input_xml_file_name = 'sample_json/EUOZJB.xml'

# Get Flattened Keys From All Records
cj = cjc.CurateJson()
with open(input_xml_file_name, encoding='utf-8-sig') as xml_file:
    for xml_row_string in xml_file:
        # convert xml to json
        json_row = xml_to_json(xml_row_string)
        # curate json (get flattened keys)
        cj.curate_json(json.dumps(json_row))
# collect flattened keys
flattened_keys = cj.get_master_dict()

# Flatten and Denormalize All Records to CSV
with open(r'output/EUOZJB_pipeline.csv', 'w') as csv_file:
    w = csv.DictWriter(csv_file, sorted(flattened_keys.keys()), lineterminator='\n', extrasaction='ignore')
    w.writeheader()

    with open(input_xml_file_name, encoding='utf-8-sig') as xml_file:
        for xml_row_string in xml_file:
            # convert xml to json
            json_row = xml_to_json(xml_row_string)
            # denormalize and flatten
            denormrows = flatten_denorm_json(json.dumps(json_row), flattened_keys)
            if denormrows is not None:
                w.writerows(denormrows)