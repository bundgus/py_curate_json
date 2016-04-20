import json
import uuid
import csv
import curate_json_core as cjc


def flatten_denorm_json(jsonstring):
    ldenormrows = []
    jsonuuid = str(uuid.uuid4())

    try:
        if jsonstring != '':
            djson = json.loads(jsonstring)
        else:
            return
    except:
        raise Exception('unparsable JSON: ' + jsonstring)
    if isinstance(djson, list):
        djson = dict(enumerate(djson))

    gn = cjc.JSONGraphNode('rootnode')
    cjc.getnodeattributes(djson, gn, atpath='')
    cjc.buildgraph(djson, gn)

    leafnodes = []

    def findleafnodes(node_to_iterate):
        if len(node_to_iterate.successors) < 1:
            leafnodes.append(node_to_iterate)
        for suc in node_to_iterate.successors:
            findleafnodes(suc)

    findleafnodes(gn)

    def crawluptree(leafnode, masterdict):
        for at in leafnode.attributes:
            masterdict[at] = leafnode.attributes[at]
        if leafnode.predecessor is not None:
            crawluptree(leafnode.predecessor, masterdict)
        masterdict['json_uuid'] = jsonuuid
        return masterdict

    for ln in leafnodes:
        consolidateddict = crawluptree(ln, attributes.copy())
        ldenormrows.append(consolidateddict.copy())

    return ldenormrows

if __name__ == "__main__":

    # load attributes dictionary
    attribute_filename = r'output/master-businessRecord_flattened_keys.json'
    with open(attribute_filename, 'r') as attributesfile:
        rawjson = attributesfile.read()
        attributes = json.loads(rawjson)

    with open(r'output/businessRecord.csv', 'w') as awf:
        # x01 is ctl-a = the default delimiter for Impala
        #w = csv.DictWriter(awf, sorted(attributes.keys()), lineterminator='\n', delimiter='\x01')
        w = csv.DictWriter(awf, sorted(attributes.keys()), lineterminator='\n', extrasaction='ignore')
        w.writeheader()

        #filename = r'sample_json/v12-businessRecord.json'
        filename = r'sample_json/analyticsWeb_SSW2010.2016-04-17-14_WCI_sswhlp1201_inst8-businessRecord.log'
        with open(filename, 'r') as f:
            for line in f:
                jstring = f.readline()
                denormrows = flatten_denorm_json(jstring)
                if denormrows is not None:
                    w.writerows(denormrows)


