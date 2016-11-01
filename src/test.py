import xmltodict
import urllib
import dicttoxml
import collections

def readOEC():
    url = "https://raw.githubusercontent.com/OpenExoplanetCatalogue/open_exoplanet_catalogue/master/systems/CoRoT-24.xml"
    data = urllib.request.urlopen(url).read().decode('utf-8')
    result = xmltodict.parse(data, dict_constructor=dict)
    return result


def dicttoXML(data):
    result = dicttoxml.dicttoxml(data, root=False, attr_type=False)
    return result




print(readOEC())
print(dicttoXML(readOEC()))