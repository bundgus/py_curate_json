# Mark Bundgus 2019
import json


class CurateJson:
    def __init__(self):
        self.masterdict = {'document_uuid': None}

    def curate_json(self, jsonstring):
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
                self.masterdict[at] = None
            if leafnode.predecessor is not None:
                crawluptree(leafnode.predecessor)

        for ln in leafnodes:
            crawluptree(ln)

    def get_master_dict(self):
        return self.masterdict

    def set_master_dict(self, json_master_dict):
        self.masterdict = json.loads(json_master_dict)


class JSONGraphNode:
    def __init__(self, nodename):
        self.nodename = nodename
        self.successors = []
        self.attributes = {}
        self.predecessor = None


def create_key(prefix, element_name):
    if prefix == '' or prefix is None:
        return '/' + str(element_name)
    else:
        return str(prefix) + '/' + str(element_name)


def getnodeattributes(jsonnode, graphnode, atpath='', element_id=None):

    if isinstance(jsonnode, dict):
        for jnodekey in jsonnode:
            jnode = jsonnode[jnodekey]

            if isinstance(jnode, dict):
                newatpath = create_key(atpath, jnodekey)
                getnodeattributes(jnode, graphnode, atpath=newatpath, element_id=1)

            elif not isinstance(jnode, list):
                newkey = create_key(atpath, jnodekey)
                graphnode.attributes[newkey] = str(jnode)
                if element_id is not None:
                    element_id_key = create_key(atpath, '@element_id')
                    graphnode.attributes[element_id_key] = element_id
    # logic for when a list has scalar values only, not a dictionary
    # e.g. "emails": ["ccc@ccc.com"]
    else:
        graphnode.attributes[atpath] = str(jsonnode)
        if element_id is not None:
            element_id_key = create_key(atpath, '@element_id')
            graphnode.attributes[element_id_key] = element_id


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
                    newkey = nodepath + '/' + jnodekey[:] + str(key)
                    newatpath = create_key(atpath, jnodekey[:])
                    newigraphnode = JSONGraphNode(newkey)

                    element_id_key = create_key(newatpath, '@element_id')
                    newigraphnode.attributes[element_id_key] = key + 1

                    newigraphnode.predecessor = parentgraphnode
                    parentgraphnode.successors.append(newigraphnode)
                    getnodeattributes(jnode[key], newigraphnode, atpath=newatpath, element_id=key + 1)
                    buildgraph(jnode[key], newigraphnode, nodepath=newkey, atpath=newatpath)
