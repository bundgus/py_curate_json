import json


class JSONGraphNode:
    def __init__(self, nodename):
        self.nodename = nodename

    successors = []
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


def create_key(prefix, element_name):
    if prefix == '':
        return str(element_name)
    else:
        return str(prefix) + '__' + str(element_name)


def drilldict(jsonnode, igraphnode, rowarray=[], elementprefix='', dictdepth=0):
    #print('elementprefix ', elementprefix)
    for key in jsonnode:
        jnode = jsonnode[key]
        key = create_key(elementprefix, key)
        if isinstance(jnode, dict):
            drilldict(jnode, igraphnode, rowarray=rowarray, elementprefix=key, dictdepth=dictdepth+1)
        elif not isinstance(jnode, list):
            key = create_key(igraphnode.nodename, key)
            #print('leafkey: ' + key + ' value: ' + str(jnode))
            igraphnode.attributes[key] = str(jnode)

    for key in jsonnode:
        jnode = jsonnode[key]
        key = create_key(elementprefix, key)
        if isinstance(jnode, list):
            # print(key)
            # print('in dict, list_element_found: ' + str(jnode))
            # todo: here is where to create new json graph node
            newigraphnode = JSONGraphNode(key)
            newigraphnode.attributes = igraphnode.attributes.copy()
            rowarray.append(newigraphnode)
            drilllist(jnode, newigraphnode, rowarray=rowarray)

    if dictdepth == 0:
        pass
        # rowarray.append(values)

    #return rowarray


def drilllist(jsonnode, igraphnode, rowarray=[]):
    for wnode in jsonnode:
        if isinstance(wnode, dict):
            # need to create new node for each array value
            newigraphnode = JSONGraphNode(igraphnode.nodename)
            newigraphnode.attributes = igraphnode.attributes.copy()
            rowarray.append(newigraphnode)
            drilldict(wnode, igraphnode, rowarray=rowarray)
        elif isinstance(wnode, list):
            print('in list, list_element_found: ' + str(wnode))
            '''
            key = create_key(igraphnode.nodename, key)
            jgraphnode = JSONGraphNode(key)
            drilllist(wnode, values.copy(), jgraphnode, rowarray=rowarray)
            '''
        else:
            '''
            key = create_key(igraphnode.nodename, wnode)
            values[key] = wnode
            '''
    #return rowarray



filename = r'sample_json/businessRecord-bookingTransaction.json'
with open(filename, 'r') as f:
    djson = json.loads(f.read())

# here is where the udf function body starts

row_list = []
jgraphnode = JSONGraphNode('')
if isinstance(djson, dict):
    drilldict(djson, jgraphnode, rowarray=row_list)
elif isinstance(djson, list):
    djson = [djson]
    drilllist(djson, jgraphnode, rowarray=row_list)


for rowdict in row_list:
    # print(rowdict)
    print('>>>>' + rowdict.nodename)
    for key in rowdict.attributes:
        if rowdict.attributes[key] is not None:
            pass
            print(key + ' -- ' + str(rowdict.attributes[key]))
    print('--------------------')

print(len(row_list))

#for key in djson:
#    print(key)


#print(djson['httpAnalytics']['clientIP'])