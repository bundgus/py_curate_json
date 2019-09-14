import xml.etree.ElementTree as Et
from io import StringIO
from .xmltodict import parse


def xml_to_dict(xml_string):
    it = Et.iterparse(StringIO(xml_string))
    for _, el in it:
        # strip all namespaces - regex approach
        # if '}' in el.tag:
        #    el.tag = re.sub(r'\{.*?\}', '', el.tag)
        if '}' in el.tag:
            el.tag = el.tag.split('}', 1)[1]  # strip all namespaces
        for a in el.attrib:
            if '}' in a:
                new_a = a.split('}', 1)[1]  # strip all namespaces
                el.attrib[new_a] = el.attrib[a]  # create new dict element
                el.attrib.pop(a)  # remove old element
    root = it.root
    # return jencoder.data(root)
    xmlstr = Et.tostring(root, encoding='utf8')
    return parse(xmlstr)
