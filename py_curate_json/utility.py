import xml.etree.ElementTree as Et
from io import StringIO
from xmljson import badgerfish as jencoder  # https://pypi.org/project/xmljson/


def xml_to_json(xml_string):
    it = Et.iterparse(StringIO(xml_string))
    for _, el in it:
        if '}' in el.tag:
            el.tag = el.tag.split('}', 1)[1]  # strip all namespaces
    root = it.root
    return jencoder.data(root)
