import datetime

def createpigpart(graph, nodename, pigstringio, predelements, first=True):

    elements = list(predelements)  # creates a copy

    for predel in predelements:
        if first is False:
            pigstringio.write('        ,')
        else:
            pigstringio.write('         ')
        first = False
        pigstringio.write(predel + '\n')

    for lkey in graph.node[nodename]:
        if first is False:
            pigstringio.write('        ,')
        else:
            pigstringio.write('         ')
        first = False
        pigstringio.write("FLATTEN($0#'{0}') as "
                          "{1}\n"
                          .format(lkey.replace('__', "'#'"), lkey))
        elements.append(lkey)
    for succe in graph.successors(nodename):
        if first is False:
            pigstringio.write('        ,')
        else:
            pigstringio.write('         ')
        first = False
        pigstringio.write("FLATTEN($0#'{0}') as "
                          "({1}:map[])\n"
                          .format(succe.replace('__', "'#'"), succe))

    return elements


def createpig(graph, nodename, pigstringio, predecessor=None, predelements=[]):
    d = datetime.datetime.now()
    savedate = str(d).replace(' ', 'T').replace(':', '-')

    # is this the root node?
    if predecessor is None:
        predecessor = 'rawline'
        pigstringio.write('''REGISTER hdfs://bdaolc011node02:8020/user/sg217516/ecommerce_checkin/json-simple-1.1.1.jar;
REGISTER hdfs://bdaolc011node02:8020/user/sg217516/ecommerce_checkin/elephant-bird-hadoop-compat-4.9.jar;
REGISTER hdfs://bdaolc011node02:8020/user/sg217516/ecommerce_checkin/elephant-bird-core-4.9.jar;
REGISTER hdfs://bdaolc011node02:8020/user/sg217516/ecommerce_checkin/elephant-bird-pig-4.9.jar;
rawline = LOAD 'hdfs://bdaolc011node02:8020/user/sg217516/ecommerce_checkin/analyticsWeb_SSW2010.2015-05-08-14_Original-businessRecord.json'
    USING com.twitter.elephantbird.pig.load.JsonLoader('-nestedLoad');
''')
    pigstringio.write('{0} = FOREACH {1} GENERATE\n'.format(nodename, predecessor))
    elements = createpigpart(graph, nodename, pigstringio, predelements)
    pigstringio.write(';\n')
    for succe in graph.successors(nodename):
        pigstringio.write("{1} = FOREACH {0} GENERATE\n     FLATTEN (rootnode#'text');\n".format(nodename, succe))
    pigstringio.write('''STORE B into 'hdfs://bdaolc011node02:8020/user/sg217516/ecommerce_checkin/analyticsweb_avro_out/analyticsWeb_{0}.avro'
  USING AvroStorage(
  ' '''.format(savedate))

    createavro(graph, 'rootnode', pigstringio)

    pigstringio.write("');")