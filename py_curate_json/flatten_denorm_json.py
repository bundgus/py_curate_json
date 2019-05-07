# Mark Bundgus 2019
import json
import uuid

from py_curate_json import curate_json_core as cjc


def flatten_denorm_json(jsonstring, attributes):
    ldenormrows = []
    recorduuid = str(uuid.uuid4())

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
            # only set value if attribute is part of masterdict
            if at in masterdict.keys():
                masterdict[at] = leafnode.attributes[at]
        if leafnode.predecessor is not None:
            crawluptree(leafnode.predecessor, masterdict)
        masterdict['document_uuid'] = recorduuid
        return masterdict

    for ln in leafnodes:
        consolidateddict = crawluptree(ln, attributes.copy())
        ldenormrows.append(consolidateddict.copy())

    return ldenormrows
