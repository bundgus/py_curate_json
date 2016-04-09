import json

attributes = {
    'ajax__actionCode': None,
    'ajax__componentType': None,
    'ancillarySelected__code': None,
    'ancillarySelected__segments__date': None,
    'ancillarySelected__segments__destination': None,
    'ancillarySelected__segments__origin': None,
    'bookingTransaction__reservation__bookingDate': None,
    'bookingTransaction__reservation__departureDate': None,
    'bookingTransaction__reservation__itinerary__itineraryParts__arrivalDate': None,
    'bookingTransaction__reservation__itinerary__itineraryParts__departureDate': None,
    'bookingTransaction__reservation__itinerary__itineraryParts__destination': None,
    'bookingTransaction__reservation__itinerary__itineraryParts__flightNumber': None,
    'bookingTransaction__reservation__itinerary__itineraryParts__origin': None,
    'bookingTransaction__reservation__itinerary__itineraryParts__segmentSize': None,
    'bookingTransaction__reservation__itinerary__itineraryParts__segments__airlineCode': None,
    'bookingTransaction__reservation__itinerary__itineraryParts__segments__arrival': None,
    'bookingTransaction__reservation__itinerary__itineraryParts__segments__arrivalAirport': None,
    'bookingTransaction__reservation__itinerary__itineraryParts__segments__bookingClass': None,
    'bookingTransaction__reservation__itinerary__itineraryParts__segments__brandId': None,
    'bookingTransaction__reservation__itinerary__itineraryParts__segments__cabinClass': None,
    'bookingTransaction__reservation__itinerary__itineraryParts__segments__departure': None,
    'bookingTransaction__reservation__itinerary__itineraryParts__segments__departureAirport': None,
    'bookingTransaction__reservation__itinerary__itineraryParts__segments__fareBasis': None,
    'bookingTransaction__reservation__itinerary__itineraryParts__segments__flightNumber': None,
    'bookingTransaction__reservation__itinerary__itineraryParts__segments__operatingAirlineCode': None,
    'bookingTransaction__reservation__itinerary__itineraryParts__totalStops': None,
    'bookingTransaction__reservation__itinerary__itineraryParts__type': None,
    'bookingTransaction__reservation__journeySpan': None,
    'bookingTransaction__reservation__passengers__ffnumber': None,
    'bookingTransaction__reservation__passengers__firstName': None,
    'bookingTransaction__reservation__passengers__lastName': None,
    'bookingTransaction__reservation__passengers__nameNumber': None,
    'bookingTransaction__reservation__passengers__passengerIndex': None,
    'bookingTransaction__reservation__passengers__emails': None,
    'bookingTransaction__reservation__payments__amount__amount': None,
    'bookingTransaction__reservation__payments__amount__currency': None,
    'bookingTransaction__reservation__payments__fopCode': None,
    'bookingTransaction__reservation__payments__paymentGateway': None,
    'bookingTransaction__reservation__payments__paymentMethod': None,
    'bookingTransaction__reservation__payments__remote': None,
    'bookingTransaction__reservation__payments__status': None,
    'bookingTransaction__reservation__payments__statusType': None,
    'bookingTransaction__reservation__pcc__channel': None,
    'bookingTransaction__reservation__pcc__code': None,
    'bookingTransaction__reservation__pcc__country': None,
    'bookingTransaction__reservation__pcc__stationNumber': None,
    'bookingTransaction__reservation__priceSummary__totalAncillaries__amount': None,
    'bookingTransaction__reservation__priceSummary__totalAncillaries__currency': None,
    'bookingTransaction__reservation__priceSummary__totalBase__amount': None,
    'bookingTransaction__reservation__priceSummary__totalBase__currency': None,
    'bookingTransaction__reservation__priceSummary__totalTax__amount': None,
    'bookingTransaction__reservation__priceSummary__totalTax__currency': None,
    'bookingTransaction__reservation__priceSummary__total__amount': None,
    'bookingTransaction__reservation__priceSummary__total__currency': None,
    'bookingTransaction__reservation__recordLocator': None,
    'bookingTransaction__reservation__route': None,
    'bookingTransaction__reservation__travelExtras__code': None,
    'bookingTransaction__reservation__travelExtras__description': None,
    'bookingTransaction__reservation__travelExtras__flightNumber': None,
    'bookingTransaction__reservation__travelExtras__passengerIndex': None,
    'bookingTransaction__reservation__travelExtras__passengerNameNumber': None,
    'bookingTransaction__reservation__travelExtras__price__amount': None,
    'bookingTransaction__reservation__travelExtras__price__currency': None,
    'bookingTransaction__reservation__travelExtras__quantity': None,
    'bookingTransaction__reservation__travelExtras__seatNumber': None,
    'bookingTransaction__reservation__travelExtras__type': None,
    'businessRecord__encode': None,
    'businessRecord__name': None,
    'businessRecord__requestType': None,
    'businessRecord__versionNumber': None,
    'debug__log4jMDC__Airline': None,
    'debug__log4jMDC__Storefront': None,
    'debug__log4jMDC__ipAddress': None,
    'httpAnalytics__airline': None,
    'httpAnalytics__ajax': None,
    'httpAnalytics__clientIP': None,
    'httpAnalytics__cookies__name': None,
    'httpAnalytics__cookies__value': None,
    'httpAnalytics__duration': None,
    'httpAnalytics__hostname': None,
    'httpAnalytics__httpMethod': None,
    'httpAnalytics__httpStatus': None,
    'httpAnalytics__ipcc': None,
    'httpAnalytics__pageCode': None,
    'httpAnalytics__referer': None,
    'httpAnalytics__requestUrl': None,
    'httpAnalytics__responseSize': None,
    'httpAnalytics__sessionID': None,
    'httpAnalytics__threadName': None,
    'httpAnalytics__timestamp': None,
    'httpAnalytics__userAgent': None,
    'httpAnalytics__visitorID': None,
    'messages__category': None,
    'messages__code': None,
    'messages__type': None,
    'pageChange__action': None,
    'pageChange__from': None,
    'pageChange__to': None,
    'storefront__airline': None,
    'storefront__channel': None,
    'storefront__configVersion': None,
    'storefront__ipcc': None,
    'storefront__owner': None,
    'user__loggedIn': None

}

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


# here is where the udf function body starts
def json_to_bag(jsonstring, denormrows):

    try:
        if jsonstring != '':
            djson = json.loads(jsonstring)
        else:
            return
    except:
        print('unparsable JSON')
        print(jsonstring)
        return
    if isinstance(djson, list):
        djson = dict(enumerate(djson))

    gn = JSONGraphNode('rootnode')
    getnodeattributes(djson, gn, atpath='')
    buildgraph(djson, gn)

    # create denormalized rows from graph

    def traversegraph(node_to_iterate, depth=0):
        print('NODE: ', end='')
        for i in range(depth):
            print('....', end='')
        print(node_to_iterate.nodename)
        #if node_to_iterate.predecessor is not None:
        #    print(node_to_iterate.predecessor.nodename)
        for a in node_to_iterate.attributes:
            print('              ', end='')
            for i in range(depth-1):
                print('    ', end='')
            print(a, node_to_iterate.attributes[a])
        print()
        for suc in node_to_iterate.successors:
            traversegraph(suc, depth=depth+1)

    #traversegraph(gn)

    leafnodes = []
    def findleafnodes(node_to_iterate):
        if len(node_to_iterate.successors) < 1:
            #print('found leaf node: ' + node_to_iterate.nodename)
            leafnodes.append(node_to_iterate)
        for suc in node_to_iterate.successors:
            findleafnodes(suc)

    findleafnodes(gn)

    def crawluptree(leafnode, masterdict):
        #print(leafnode.nodename)
        for at in leafnode.attributes:
            #print(at, leafnode.attributes[at])
            masterdict[at] = leafnode.attributes[at]
        if leafnode.predecessor is not None:
            crawluptree(leafnode.predecessor, masterdict)
        return masterdict

    #print('crawling up leaf nodes')
    for ln in leafnodes:
        consolidateddict = crawluptree(ln, attributes.copy())
        #print(consolidateddict)
        denormrows.append(consolidateddict.copy())

    #for row in denormrows:
        # print(row)

    return denormrows

if __name__ == "__main__":
    agdenormrows = []
    filename = r'sample_json/analyticsWeb_SSW2010.2015-05-08-14_Original-businessRecord.json'
    with open(filename, 'r') as f:
        for line in f:
            jstring = f.readline()
            json_to_bag(jstring, agdenormrows)

    import csv
    with open('analyticsweb.csv', 'a') as awf:
        w = csv.DictWriter(awf, attributes.keys(), lineterminator='\n')
        w.writeheader()
        w.writerows(agdenormrows)
