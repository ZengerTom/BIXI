import webbrowser


def openRoute(lat1,lat2,lat3,lat4,lng1,lng2,lng3,lng4):
    f = open('biximap.html', 'w')

    latC = 43.6499538
    latO = lat1
    latE = lat2
    latBS = lat3
    latRS = lat4

    lngC = -79.3886734
    lngO = lng1
    lngE = lng2
    lngBS = lng3
    lngRS = lng4

    message = """<!DOCTYPE html>
    <html>
    <head>
        <title>BIXI Map</title>
        <meta name="viewport" content="initial-scale=1.0">
        <meta charset="utf-8">
        <style>
          html, body {
            height: 100%;
            margin: 0;
            padding: 0;
        }
        #map {
            height: 100%;
          }
        </style>
    </head>
    <body>
        <div id="map"></div>
        <script>

    var map;
    function initMap() {
    var directionsService = new google.maps.DirectionsService;
    var directionsDisplay = new google.maps.DirectionsRenderer;
    var ctLatLng = {lat: 43.6499538, lng: -79.3886734};
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: """ + str(latC) + """, lng: """ + str(lngC) + """},
        zoom: 14
    });
    directionsDisplay.setMap(map);
    calcRoute(directionsService, directionsDisplay);

    }

    function calcRoute(directionsService, directionsDisplay) {

    var start = {lat: """ + str(latO) + """, lng: """ + str(lngO) + """};
    var end = {lat: """ + str(latE) + """, lng: """ + str(lngE) + """};
    var waypts = [];
    bs = new google.maps.LatLng(""" + str(latBS) + """,""" + str(lngBS) + """)
    waypts.push({
    location: bs,
    stopover: true
    });

    rs = new google.maps.LatLng(""" + str(latRS) + """,""" + str(lngRS) + """)

    waypts.push({
    location: rs,
    stopover: true
    });

      directionsService.route({
        origin: start,
        destination: end,
        waypoints: waypts,
    optimizeWaypoints: true,
        travelMode: google.maps.TravelMode.WALKING
    }, function(response, status) {
        if (status === google.maps.DirectionsStatus.OK) {
          directionsDisplay.setDirections(response);
           var route = response.routes[0];
      for (var i = 0; i < route.legs.length; i++) {
        var routeSegment = i + 1;

      }
        } else {
        window.alert('Directions request failed due to ' + status);
        }
    });
    }

        </script>

        <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCUb2IbVRBmNEsAx9agXSeo5qmJVj61VoU&signed_in=true&callback=initMap"
            async defer></script>
    </body>
    </html>"""

    f.write(message)
    f.close()

    filename = 'biximap.html'
    webbrowser.open(filename)
