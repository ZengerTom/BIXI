class Station:
    nbStations = 0

    def __init__(self, ident, name, lat, long, installed, locked, public, nbBikes, nbEmptyDocks):
        self.__ident = ident
        self.__name = name
        self.__lat = lat
        self.__long = long
        self.__installed = installed
        self.__locked = locked
        self.__public = public
        self.__nbBikes = nbBikes
        self.__nbEmptyDocks = nbEmptyDocks
        Station.nbStations += 1

    def __del__(self):
        Station.nbStations -= 1

    def getIdent(self):
        return self.__ident

    def getName(self):
        return self.__name

    def getLat(self):
        return self.__lat

    def getLong(self):
        return self.__long

    def getLocked(self):
        return self.__locked

    def getInstalled(self):
        return self.__installed

    def getPublic(self):
        return self.__public

    def getBikes(self):
        return self.__nbBikes

    def getDocks(self):
        return self.__nbEmptyDocks

    def getAll(self):
        return self.getIdent(), self.getName(), self.getTerminalName(), self.getLat(), self.getLong(), self.getLocked(), self.getInstalled(), self.getPublic(), self.getBikes(), self.getDocks()
