import json
import uuid

class JSONGraphNode:
    def __init__(self, nodename):
        self.nodename = nodename
        self.successors = []
        self.attributes = {}
        self.predecessor = None


def create_key(prefix, element_name):
    if prefix == '' or prefix is None:
        return str(element_name)
    else:
        return str(prefix) + '__' + str(element_name)


def getnodeattributes(jsonnode, graphnode, atpath=''):

    if isinstance(jsonnode, dict):
        for jnodekey in jsonnode:
            jnode = jsonnode[jnodekey]

            if isinstance(jnode, dict):
                newatpath = create_key(atpath, jnodekey)
                getnodeattributes(jnode, graphnode, atpath=newatpath)

            elif not isinstance(jnode, list):
                newkey = create_key(atpath, jnodekey)
                graphnode.attributes[newkey] = str(jnode)
    # logic for when a list has scalar values only, not a dictionary
    # e.g. "emails": ["ccc@ccc.com"]
    else:
        #print(jsonnode)
        graphnode.attributes[atpath] = str(jsonnode)


def buildgraph(jsonnode, parentgraphnode, nodepath='', atpath=''):

    if isinstance(jsonnode, dict):
        for jnodekey in jsonnode:
            jnode = jsonnode[jnodekey]
            if isinstance(jnode, dict):
                newnodepath = create_key(nodepath, jnodekey)
                newatpath = create_key(atpath, jnodekey)
                buildgraph(jnode, parentgraphnode, nodepath=newnodepath, atpath=newatpath)

            elif isinstance(jnode, list):
                jnode = dict(enumerate(jnode))
                for key in jnode:
                    newkey = nodepath + '__' + jnodekey[:] + str(key)
                    newatpath = create_key(atpath, jnodekey[:])
                    newigraphnode = JSONGraphNode(newkey)
                    newigraphnode.predecessor = parentgraphnode
                    parentgraphnode.successors.append(newigraphnode)
                    getnodeattributes(jnode[key], newigraphnode, atpath=newatpath)
                    buildgraph(jnode[key], newigraphnode, nodepath=newkey, atpath=newatpath)


masterdict = {}


def curate_json(jsonstring):
    denormrows = []
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

    gn = JSONGraphNode('rootnode')
    getnodeattributes(djson, gn, atpath='')
    buildgraph(djson, gn)

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
        denormrows.append(consolidateddict.copy())

    return denormrows

if __name__ == "__main__":
    filename = r'sample_json/v12-businessRecord.json'

    agdenormrows =[]
    with open(filename, 'r') as f:
        for line in f:
            jstring = f.readline()
            denormrows = curate_json(jstring)
            if denormrows is not None:
                agdenormrows.extend(denormrows)

    for key in masterdict:
        masterdict[key] = None

    with open(r'output/businessRecord_flattened_keys.json', 'w') as fk:
        fk.write(json.dumps(masterdict, sort_keys=True, indent=4, separators=(',', ': ')))
    print('flat schema written to output/businessRecord_flattened_keys.json')
