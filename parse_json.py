import json
import uuid

attributes = {
'json_uuid': None,
'ajax__actionCode': None,
'ajax__componentType': None,
'bookingTransaction__loggedUser__ffnumber': None,
'bookingTransaction__loggedUser__firstName': None,
'bookingTransaction__loggedUser__lastName': None,
'bookingTransaction__loggedUser__prefix': None,
'bookingTransaction__loggedUser__tierLevel': None,
'bookingTransaction__loggedUser__emails': None,
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
'bookingTransaction__reservation__passengers__memberAirline': None,
'bookingTransaction__reservation__passengers__nameNumber': None,
'bookingTransaction__reservation__passengers__passengerIndex': None,
'bookingTransaction__reservation__passengers__prefix': None,
'bookingTransaction__reservation__passengers__tierLevel': None,
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
'bookingTransaction__reservation__travelExtras__flightNumber': None,
'bookingTransaction__reservation__travelExtras__passengerIndex': None,
'bookingTransaction__reservation__travelExtras__passengerNameNumber': None,
'bookingTransaction__reservation__travelExtras__price__amount': None,
'bookingTransaction__reservation__travelExtras__price__currency': None,
'bookingTransaction__reservation__travelExtras__quantity': None,
'bookingTransaction__reservation__travelExtras__seatNumber': None,
'bookingTransaction__reservation__travelExtras__type': None,
'buildInfo__branch': None,
'buildInfo__buildId': None,
'buildInfo__jobName': None,
'buildInfo__releaseName': None,
'buildInfo__revisionNumber': None,
'buildInfo__version': None,
'businessRecord__encode': None,
'businessRecord__name': None,
'businessRecord__requestType': None,
'businessRecord__versionNumber': None,
'cartAnalytics__cartItineraryParts__arrivalAirport': None,
'cartAnalytics__cartItineraryParts__arrivalDate': None,
'cartAnalytics__cartItineraryParts__bookingClass': None,
'cartAnalytics__cartItineraryParts__departureAirport': None,
'cartAnalytics__cartItineraryParts__departureDate': None,
'cartAnalytics__cartItineraryParts__fareBasis': None,
'cartAnalytics__cartItineraryParts__numberOfStops': None,
'cartAnalytics__cartItineraryParts__operatingCarrier': None,
'cartAnalytics__cartItineraryParts__flightNumber': None,
'cartAnalytics__cartItineraryParts__stops': None,
'cartAnalytics__currencyCode': None,
'cartAnalytics__journeySpan': None,
'cartAnalytics__priceSummary__totalBase__amount': None,
'cartAnalytics__priceSummary__totalBase__currency': None,
'cartAnalytics__priceSummary__totalTax__amount': None,
'cartAnalytics__priceSummary__totalTax__currency': None,
'cartAnalytics__priceSummary__total__amount': None,
'cartAnalytics__priceSummary__total__currency': None,
'httpAnalytics__airline': None,
'httpAnalytics__ajax': None,
'httpAnalytics__clientIP': None,
'httpAnalytics__duration': None,
'httpAnalytics__executionId': None,
'httpAnalytics__hostname': None,
'httpAnalytics__httpMethod': None,
'httpAnalytics__httpStatus': None,
'httpAnalytics__instance': None,
'httpAnalytics__ipcc': None,
'httpAnalytics__pageCode': None,
'httpAnalytics__referer': None,
'httpAnalytics__requestUrl': None,
'httpAnalytics__responseHeaders__location': None,
'httpAnalytics__responseSize': None,
'httpAnalytics__sessionID': None,
'httpAnalytics__snapshotId': None,
'httpAnalytics__threadName': None,
'httpAnalytics__timestamp': None,
'httpAnalytics__userAgent': None,
'httpAnalytics__visitorID': None,
'messages__category': None,
'messages__code': None,
'messages__type': None,
'messages__messages': None,
'messages__stackTrace': None,
'pageChange__action': None,
'pageChange__from': None,
'pageChange__to': None,
'shopping__duration': None,
'shopping__searchCriteria__cabin': None,
'shopping__searchCriteria__daysToDeparture': None,
'shopping__searchCriteria__departureDates': None,
'shopping__searchCriteria__journeySpan': None,
'shopping__searchCriteria__originDestinations__date': None,
'shopping__searchCriteria__originDestinations__destination': None,
'shopping__searchCriteria__originDestinations__origin': None,
'shopping__searchCriteria__passengers__ADT': None,
'shopping__searchCriteria__routes': None,
'shopping__searchCriteria__searchType': None,
'shopping__searchCriteria__stayDurationInDays': None,
'shopping__searchCriteria__airports': None,
'storefront__airline': None,
'storefront__channel': None,
'storefront__configVersion': None,
'storefront__ipcc': None,
'storefront__owner': None,
'user__loggedIn': None,
'user__person__firstName': None,
'user__person__lastName': None,
'user__username': None
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
def json_to_bag(jsonstring):
    denormrows = []
    jsonuuid = str(uuid.uuid4())

    try:
        if jsonstring != '':
            djson = json.loads(jsonstring)
        else:
            return
    except:
        raise Exception('unparsable JSON: ' + jsonstring)
        return
    if isinstance(djson, list):
        djson = dict(enumerate(djson))

    gn = JSONGraphNode('rootnode')
    getnodeattributes(djson, gn, atpath='')
    buildgraph(djson, gn)

    # create denormalized rows from graph

    '''
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
    '''

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
        masterdict['json_uuid'] = jsonuuid
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
    #filename = r'sample_json/analyticsWeb_SSW2010.2015-05-08-14_Original-businessRecord.json'
    filename = r'sample_json/v12-businessRecord.json'

    agdenormrows =[]
    with open(filename, 'r') as f:
        for line in f:
            jstring = f.readline()
            denormrows = json_to_bag(jstring)
            if denormrows is not None:
                agdenormrows.extend(denormrows)

    for key in sorted(attributes.keys()):
        print(key+' STRING,')

    import csv
    with open('v12_businessRecord.csv', 'w') as awf:
        w = csv.DictWriter(awf, sorted(attributes.keys()), lineterminator='\n', delimiter='\x01')
        #w = csv.DictWriter(awf, sorted(attributes.keys()), lineterminator='\n')
        w.writeheader()
        w.writerows(agdenormrows)
