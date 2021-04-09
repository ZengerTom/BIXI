class Route_2p:
    def __init__(self, origin, destination, duration, distance):
        self.__origin = origin
        self.__destination = destination
        self.__duration = duration
        self.__distance = distance

    def __del__(self):
        return

    def getOrigin(self):
        return self.__origin

    def getDestination(self):
        return self.__destination

    def getDuration(self):
        return self.__duration

    def getDistance(self):
        return self.__distance

    def getAll(self):
        return self.getOrigin(), self.getDestination(), self.getDuration(), self.getDistance()
