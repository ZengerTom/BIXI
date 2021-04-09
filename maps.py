import resultParser as rp

key = "AIzaSyCUb2IbVRBmNEsAx9agXSeo5qmJVj61VoU"


def getUrl(lat1, long1, lat2, long2, travelmode):
    url = "https://maps.googleapis.com/maps/api/distancematrix/xml?origins=" + lat1 + "," + long1 + "&destinations=" + lat2 + "," + long2 + "&key=" + key + "&mode=" + travelmode + "&units=metric"
    return url


def getUrl_string(orig, dest, travelmode):
    url = "https://maps.googleapis.com/maps/api/distancematrix/xml?origins=" + orig + "&destinations=" + dest + "&key=" + key + "&mode=" + travelmode + "&units=metric"
    return url


def getUrl_mixed(orig, lat2, long2, travelmode):
    url = "https://maps.googleapis.com/maps/api/distancematrix/xml?origins=" + orig + "&destinations=" + lat2 + "," + long2 + "&key=" + key + "&mode=" + travelmode + "&units=metric"
    return url


def getDistance(lat1, long1, lat2, long2, travelmode):
    url = getUrl(lat1, long1, lat2, long2, travelmode)
    route = rp.route2(url)
    return route.getDistance()


def getDistance_string(orig, dest, travelmode):
    url = getUrl_string(orig, dest, travelmode)
    route = rp.route2(url)
    return route.getDistance()


def getDistance_mixed(orig, lat2, long2, travelmode):
    url = getUrl_mixed(orig, lat2, long2, travelmode)
    route = rp.route2(url)
    return route.getDistance()

def getLatLng(adress):
    url = "https://maps.googleapis.com/maps/api/geocode/xml?address="+adress+"&key="+key
    latLng = rp.geocoding(url)
    return latLng

