from __future__ import with_statement
import json
import networkx as nx
import io
import datetime
from create_avro_schema import createavroschema
from create_json_to_parquet_pig_script import create_json_to_parquet_pig_script
from create_pig_udf import create_pig_udf
from create_json_schema import create_json_schema
from create_schema_outline import create_schema_outline

debugflag = False


def debug(debugmessage):
    if debugflag is True:
        print(debugmessage)


def drilldict(jsonnode, myG, nodename, nodeprefix):
    for key in jsonnode:
        if isinstance(jsonnode[key], dict):
            debug(key + 'found a dict inside a dict')
            if nodeprefix == '':
                drilldict(jsonnode[key], myG, nodename, key)
            else:
                drilldict(jsonnode[key], myG, nodename, nodeprefix + '__' + key)
        elif isinstance(jsonnode[key], list):
            debug('found a list inside a dict ' + key)
            if nodeprefix == '':
                myG.add_edge(nodename, key)
                drilllist(jsonnode[key], myG, key, key)
            else:
                myG.add_edge(nodename, nodeprefix + '__' + key)
                drilllist(jsonnode[key], myG, nodeprefix + '__' + key, nodeprefix)
        else:
            debug('found an element inside a dict ' + nodeprefix + ' ' + key)
            if nodeprefix == '':
                myG.node[nodename][key] = jsonnode[key]
            else:
                myG.node[nodename][nodeprefix + '__' + key] = jsonnode[key]


def drilllist(jsonnode, myG, nodename, nodeprefix):
    for i, wnode in enumerate(jsonnode):
        if isinstance(wnode, dict):
            debug('found a dict inside a list' + ' ' + nodename + ' ' + nodeprefix)
            if nodeprefix == '':
                drilldict(jsonnode[i], myG, nodename, nodename)
            else:
                drilldict(jsonnode[i], myG, nodename, nodename)
        elif isinstance(wnode, list):
            debug('found a list inside a list', nodename, nodeprefix)
        else:
            # TODO: add logic for when a list has scalar values only, not a dictionary
            debug('found an element inside a list ' + wnode)


def create_flattened_list(graph, nodename='rootnode', parts=[]):
    for lkey in graph.node[nodename]:
        parts.append(lkey)
    for succe in graph.successors(nodename):
        create_flattened_list(graph, nodename=succe, parts=parts)
    return parts

if __name__ == "__main__":

    prefixname = 'businessRecord'
    filename = r'sample_json/analyticsWeb_SSW2010.2015-05-08-14_Original-businessRecord.json'

    # First let's build a digraph of lists from the JSON samples (one JSON of the same schema type per line)
    G = nx.DiGraph()
    with open(filename, 'r') as f:
        G.add_node('rootnode')
        for rawjson in f:
            rjson = json.loads(rawjson)
            # start at the root node of the JSON
            drilldict(rjson, G, 'rootnode', '')

    # get flattened list of elements
    partlist = create_flattened_list(G)
    partlist.sort()

    #create_json_schema(G, prefixname=prefixname)
    #createavroschema(G, 'rootnode')
    create_json_to_parquet_pig_script(G, parts=partlist, prefixname=prefixname)
    create_pig_udf(G, parts=partlist, prefixname=prefixname)
    create_schema_outline(G)
