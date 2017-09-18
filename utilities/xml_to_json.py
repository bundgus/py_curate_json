import xml.etree.ElementTree as ET
from xmljson import yahoo as jencoder
from json import dumps

ns = {'asds4_0': 'http://services.sabre.com/res/asds/v4_0',
      'stl15': 'http://webservices.sabre.com/pnrbuilder/v1_15',
      'ns18': 'http://services.sabre.com/res/or/v1_8'}


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


xml_tree = ET.parse('EUOZJB.xml').getroot()

set_prefixes(xml_tree, ns)

d = jencoder.data(xml_tree)
print(dumps(d))

with open(r'EUOZJB.json', 'w') as json_file:
    json_file.write(dumps(d))
