import io


def avroprimative(value):
    if isinstance(value, str):
        return 'string'
    if isinstance(value, bool):
        return 'string'
    if isinstance(value, int):
        return 'string'
    return 'string'


def createavropart(graph, nodename, avrostringio, first=True):
    for lkey in graph.node[nodename]:
        if first is False:
            avrostringio.write(',')
        first = False
        avrostringio.write('''
      {{
        "name": "{0}",
        "type": [
          "null",
          "{1}"
        ],
        "default": null
      }}'''.format(lkey, avroprimative(graph.node[nodename][lkey])))


def createavroschema(graph, nodename):
    avrostringio = io.StringIO()
    avrostringio.write('''{
    "namespace": "ecommercecheckin.sabre.com",
    "type": "record",
    "name": "ecommercecheckin",
    "fields": [''')

    createavropart(graph, 'rootnode', avrostringio)

    avrostringio.write('''
    ]
}''')
    with open(r'output\json_avro_schema.avsc', 'w') as outfile:
        outfile.write(avrostringio.getvalue())