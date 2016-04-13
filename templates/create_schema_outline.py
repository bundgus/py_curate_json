import io


def listnodes(graph, nodename, ios, depth=0):
    for i in range(0, depth):
        ios.write('----')
    ios.write(nodename)
    ios.write('\n')
    for lkey in graph.node[nodename]:
        for i in range(0, depth+1):
            ios.write('    ')
        ios.write(lkey + ':')
        ios.write(str(type(graph.node[nodename][lkey])))
        ios.write('\n')
    for succe in graph.successors(nodename):
        listnodes(graph, succe, ios, depth=depth+1)


def create_schema_outline(graph, nodename='rootnode'):
    sio = io.StringIO()
    listnodes(graph, nodename, sio)
    with open(r'output\schema_outline.txt', 'w') as outfile:
        outfile.write(sio.getvalue())