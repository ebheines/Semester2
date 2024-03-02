
class Robot:
    def __init__(self, inbox, outbox, position):
        self.inbox =  []
        self.outbox = []
        self.position = position
    
    def send_msg_to_robot_operators(self, msg):
        self.inbox.append(msg)
    

class Drone(Robot):
    def __init__(self, flight_time, images):
        self.inbox =  []
        self.outbox = []
        self.position = []
        super().__init__(self.inbox, self.outbox, self.position)
        self.flight_time = flight_time
        self.images = images
    

class AirQualityDrone(Robot):
    def __init__(self, flight_time, images):
        self.inbox =  []
        self.outbox = []
        self.position = []
        super().__init__(self.inbox, self.outbox, self.position)
        self.flight_time = flight_time
        self.images = images
        self.air_quality_log = []


class Rover(Robot):
    def __init__(self, cargo):
        self.inbox =  []
        self.outbox = []
        self.position = []
        super().__init__(self.inbox, self.outbox, self.position)
        self.cargo = cargo
        self.sensorlist = []


class Sensor(Robot):
    def __init__(self, sensordata):
        self.inbox =  []
        self.outbox = []
        self.position = []
        super().__init__(self.inbox, self.outbox, self.position)
        self.sensordata = sensordata


class Sitemanager:
    def __init__(self):
        self.splist = []

    def add_sensor(self, sensorobj):
        self.splist.append(sensorobj)


if __name__ == "__main__":
    aqdrone = AirQualityDrone(2, None)


