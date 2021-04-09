import gui
from PyQt4 import QtGui, QtCore
import sys
import routing
import nearest as near
import maps
import parse as ps
import examples as ex


#url = "http://feeds.bikesharetoronto.com/stations/stations.xml"
url = "https://www.thomas-zenger.de/data/stations.xml"

travel = {"walking": "walking", "bicycling": "bicycling"}
option = {"bike": True, "dock": False}


class Controller(QtGui.QMainWindow, gui.Ui_BIXIMap):

    def __init__(self, parent=None):
        super(Controller, self).__init__(parent)
        self.setupUi(self)
        self.updt()

        #Fill CB with items
        ex.fillBox(self.edit_orig)
        ex.fillBox(self.edit_dest)

        #Validator etc.
        self.edit_k.setMaxLength(3)
        self.edit_dest.lineEdit().setMaxLength(25)
        self.edit_orig.lineEdit().setMaxLength(25)
        validator = QtGui.QIntValidator(0, 999)
        self.edit_k.setValidator(validator)
        rex = QtCore.QRegExp("\d{1,3},\s[a-zA-Z0-9 ]*")
        regVal = QtGui.QRegExpValidator(rex)
        self.edit_orig.setValidator(regVal)
        self.edit_dest.setValidator(regVal)

        # Slots, Signals etc.
        self.edit_orig.editTextChanged.connect(self.indexOrig)
        self.edit_dest.editTextChanged.connect(self.indexDesti)
        self.edit_orig.currentIndexChanged.connect(self.indexCh)
        self.edit_dest.currentIndexChanged.connect(self.indexCh)
        self.connect(self.btn_bike, QtCore.SIGNAL("clicked()"), self.onBike)
        self.connect(self.btn_station, QtCore.SIGNAL("clicked()"), self.onStation)
        self.connect(self.btn_route, QtCore.SIGNAL("clicked()"), self.onRoute)

    def indexOrig(self):
        self.indexO = 0

    def indexDesti(self):
        self.indexD = 0

    def inputHandler(self):

        if (self.indexO == 0 and self.indexD == 0):

            temp = str(self.edit_orig.currentText())
            temp = temp.replace(", ","+")
            temp = temp.replace(" ", "+")
            location = temp+"+toronto+ca"
            temp = str(self.edit_dest.currentText())
            temp = temp.replace(", ", "+")
            temp = temp.replace(" ", "+")
            dest = temp+"toronto+ca"

        elif (self.indexO == 0 and self.indexD != 0):

            temp = str(self.edit_orig.currentText())
            temp = temp.replace(", ", "+")
            temp = temp.replace(" ", "+")
            location = temp + "+toronto+ca"
            dest = str(self.edit_dest.itemData(self.indexD))

        elif (self.indexD == 0 and self.indexO != 0):

            location = str(self.edit_orig.itemData(self.indexO))
            temp = str(self.edit_dest.currentText())
            temp = temp.replace(", ", "+")
            temp = temp.replace(" ", "+")
            dest = temp + "toronto+ca"

        else:

            location = self.edit_orig.itemData(self.indexO)
            dest = self.edit_dest.itemData(self.indexD)

        return location, dest

    def indexCh (self):
        self.indexO = self.edit_orig.currentIndex()
        self.indexD = self.edit_dest.currentIndex()

    def onBike(self):
        self.output.clear()
        self.output.append("Something went terrible wrong!")
        self.output.append("Please check your input and try it again!")
        self.bike(travel["walking"], option["bike"])

    def onStation(self):
        self.output.clear()
        self.output.append("Something went terrible wrong!")
        self.output.append("Please check your input and try it again!")
        self.bike(travel["bicycling"], option["dock"])

    def onRoute(self):
        self.output.clear()
        input = self.inputHandler()
        loc = input[0]
        dest = input[1]

        self.output.append("Something went terrible wrong!")
        self.output.append("Please check your input and try it again!")
        location = maps.getLatLng(loc)
        destination = maps.getLatLng(dest)
        stations = ps.getStations(url)
        nearestBS = near.getNearestStation(loc, stations, travel["walking"], option["bike"])
        nearestRS = near.getNearestStation(dest, stations, travel['walking'], option["dock"])
        wpBS = near.getLocation(nearestBS[0], stations)
        wpRS = near.getLocation(nearestRS[0], stations)
        routing.openRoute(str(location[0]),str(destination[0]),str(wpBS[0]),str(wpRS[0]),str(location[1]),str(destination[1]),str(wpBS[1]),str(wpRS[1]),)
        self.output.clear()
        self.output.append("A: Origin Address")
        self.output.append("B: Bike Station")
        self.output.append("C: Return Station")
        self.output.append("D: Destination Address")


    def updt(self):
        count = len(ps.getStations(url))
        self.station_label.setText("Actual we list " + str(count) + " bike stations you are free to use")

    def bike(self, trav, opt):

        k = self.edit_k.text()

        input = self.inputHandler()
        loc = input[0]

        stations = ps.getStations(url)
        focus = near.getNearestStation(loc, stations, trav, opt)
        self.output.clear()
        self.output.append("Hello " + str(k) + ", the next station is " + str(focus[1]) + " meters away")
        self.output.append("Station: " + str(focus[0]))
        self.output.append("Have a nice day!")


def main():
        app = QtGui.QApplication(sys.argv)
        mainW = Controller()
        mainW.show()
        sys.exit(app.exec_())

