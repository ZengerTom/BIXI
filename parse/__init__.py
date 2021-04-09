from xml.dom.minidom import *
import urllib.request
import station as st


def createStation(list):
    stat = st.Station(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8])
    return stat


def getValues(node):
    list = []
    rng = (1, 3, 9, 11, 13, 21, 23, 25, 27)
    for a in rng:
            act = node.item(a)
            list.append(act.firstChild.nodeValue)
    return list


def urlParser(url):
    xml = urllib.request.urlopen(url).read()

    dom = parseString(xml)
    root = dom._get_documentElement()
    return root


def getStations(url):
    root = urlParser(url)
    stationList = []
    sp = root.getElementsByTagName("station")
    fst = sp.item(0).childNodes

    stationList.append(createStation(getValues(fst)))
    for i in range(0, sp.length - 1):
       foc = sp.item(i).childNodes
       stationList.append(createStation(getValues(foc)))

    return stationList
