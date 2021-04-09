from xml.dom.minidom import *
import urllib.request
import route_2p as ro


def urlParser(url):
    xml = urllib.request.urlopen(url).read()
    dom = parseString(xml)
    root = dom._get_documentElement()
    return root


def route2(url):
    root = urlParser(url)
    origin = root.getElementsByTagName("origin_address").item(0).firstChild.nodeValue
    destination = root.getElementsByTagName("destination_address").item(0).firstChild.nodeValue
    ele = root.getElementsByTagName("row").item(0).childNodes.item(1).childNodes
    try:
        duration_s = ele.item(3).childNodes.item(1).firstChild.nodeValue
        distance_m = ele.item(5).childNodes.item(1).firstChild.nodeValue
    except AttributeError:
        duration_s = 10000000;
        distance_m = 10000000;
    route = ro.Route_2p(origin, destination, duration_s, distance_m)
    return route


def geocoding(url):
    root = urlParser(url)
    lat = root.getElementsByTagName("location").item(0).getElementsByTagName("lat").item(
        0).firstChild.nodeValue
    lng = root.getElementsByTagName("location").item(0).getElementsByTagName("lng").item(
        0).firstChild.nodeValue
    return lat, lng