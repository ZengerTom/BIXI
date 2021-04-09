import maps as mp
import operator

def findStation(stations, index):
    for station in stations:
        i = station.getIdent()
        if int(i) == index:
            return station


def getDistances(orig, stations, travelmode):
    distList = []
    for station in stations:
        if (station.getLocked() == "false" and station.getPublic() == "true" and station.getInstalled() == "true"):
            lat = station.getLat()
            long = station.getLong()
            dist = mp.getDistance_mixed(orig, lat, long, travelmode)
            result = (int(station.getIdent()), int(dist))
            distList.append(result)
    distList.sort(key=operator.itemgetter(1), reverse=True)
    return distList


def getNearestStation(orig, stations, travelmode, option):
    x = False
    distList = getDistances(orig, stations, travelmode)

    while x == False:
        near = distList.pop()
        station = findStation(stations, near[0])
        if option == True:
            x = bikeAvail(station)
        if option == False:
            x = dockAvail(station)

    return station.getName(), near[1]


def bikeAvail(station):
    if int(station.getBikes()) > 0:
        return True
    else:
        return False


def dockAvail(station):
    if int(station.getDocks()) > 0:
        return True
    else:
        return False

def getLocation(name, stations):
    for station in stations:
        i = station.getName()
        if i == name:
            return station.getLat(),station.getLong()