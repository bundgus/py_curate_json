import json


class JSONGraphNode:
    def __init__(self, nodename):
        self.nodename = nodename

    successors = []
    predecessor = None
    nodename = ''
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


class JSONGraph:
    elements = {}

    def addnode(self, newnode):
        self.elements[newnode.nodename] = newnode


def create_key(prefix, element_name):
    if prefix == '':
        return str(element_name)
    else:
        return str(prefix) + '__' + str(element_name)


def drilldict(jsonnode, igraphnode, graph, elementprefix='', dictdepth=0):
    for jkey in jsonnode:
        jnode = jsonnode[jkey]
        jkey = create_key(elementprefix, jkey)
        if isinstance(jnode, dict):
            drilldict(jnode, igraphnode, graph, elementprefix=jkey, dictdepth=dictdepth+1)
        elif not isinstance(jnode, list):
            #jkey = create_key(igraphnode.nodename, jkey)
            igraphnode.attributes[jkey] = str(jnode)

    for jkey in jsonnode:
        jnode = jsonnode[jkey]
        jkey = create_key(elementprefix, jkey)
        if isinstance(jnode, list):
            # here is where to create new json graph node
            newigraphnode = JSONGraphNode(jkey[:])
            # newigraphnode.attributes = igraphnode.attributes.copy()
            newigraphnode.predecessor = igraphnode.nodename
            graph.addnode(newigraphnode)
            #rowarray.append(newigraphnode)
            drilllist(jnode, newigraphnode, graph)


def drilllist(jsonnode, igraphnode, graph):
    for wnode in jsonnode:
        if isinstance(wnode, dict):
            # need to create new node for each array value
            newigraphnode = JSONGraphNode(igraphnode.nodename[:])
            # newigraphnode.attributes = igraphnode.attributes.copy()
            newigraphnode.predecessor = igraphnode.nodename
            graph.addnode(newigraphnode)
            # rowarray.append(newigraphnode)
            drilldict(wnode, newigraphnode, graph, elementprefix=igraphnode.nodename)


# here is where the udf function body starts
def json_to_bag(jsonstring):
    #  TODO: CREATE GRAPH (DICT) TO STORE GRAPHNODES?  EVERY NODE WITHOUT CHILDREN IS A NEW ROW...?

    djson = json.loads(jsonstring)

    jg = JSONGraph()
    jgraphnode = JSONGraphNode('')
    jg.addnode(jgraphnode)

    if isinstance(djson, dict):
        drilldict(djson, jgraphnode, jg)
    elif isinstance(djson, list):
        djson = [djson]
        drilllist(djson, jgraphnode, jg)

    for node in jg.elements:
        print(node)
        for attribute in jg.elements[node].attributes:
            if jg.elements[node].attributes[attribute] is not None:
                print('--> ', attribute, jg.elements[node].attributes[attribute])



filename = r'sample_json/businessRecord-bookingTransaction.json'
with open(filename, 'r') as f:
    jstring = f.read()
    json_to_bag(jstring)
