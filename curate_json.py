import json
import uuid
import curate_json_core as cjc


def curate_json(jsonstring):
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

    def crawluptree(leafnode):
        for at in leafnode.attributes:
            masterdict[at] = leafnode.attributes[at]
        if leafnode.predecessor is not None:
            crawluptree(leafnode.predecessor)
        masterdict['json_uuid'] = jsonuuid
        return masterdict

    for ln in leafnodes:
        consolidateddict = crawluptree(ln)
        ldenormrows.append(consolidateddict)

    return ldenormrows


masterdict = {}

if __name__ == "__main__":
    filename = r'sample_json/json_sample.json'

    agdenormrows =[]
    with open(filename, 'r') as f:
        for line in f:
            print(line)
            denormrows = curate_json(line)
            if denormrows is not None:
                agdenormrows.extend(denormrows)

    for key in masterdict:
        masterdict[key] = None

    with open(r'output/json_sample_flattened_keys.json', 'w') as fk:
        fk.write(json.dumps(masterdict, sort_keys=True, indent=4, separators=(',', ': ')))
