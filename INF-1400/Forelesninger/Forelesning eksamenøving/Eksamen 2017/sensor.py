
# Some of the attributes are common for all of the classes.
# I choose to put these attributes in an own class, Robot, 
# which all the other classes can inherit from. This makes the
# program easier to read and understand. The attributes that
# are unique to each class is added in that spesific class.

class Robot:
    def __init__(self, position) -> None:
        self.inbox = []
        self.outbox = []
        self.position = position
    


class Drone(Robot):
    def __init__(self, inbox, outbox, position, flight_time, images) -> None:
        super().__init__(inbox, outbox, position)
        self.flight_time = flight_time
        self.images = images
        

class AirQualityDrone(Robot):
    def __init__(self, inbox, outbox, position, flight_time, images, air_quality_log) -> None:
        super().__init__(inbox, outbox, position)
        self.flight_time = flight_time
        self.images = images
        self.air_quality_log = air_quality_log
    

class Rover(Robot):
    def __init__(self, inbox, outbox, position, cargo) -> None:
        super().__init__(inbox, outbox, position)
        self.cargo = cargo
        self.sensorlist = []

class Sensor(Robot):
    def __init__(self, inbox, outbox, position, sensor_data) -> None:
        super().__init__(inbox, outbox, position)
        self.sensor_data = sensor_data

class SiteManager:
    def __init__(self) -> None:
        self.splist = []
    
    def add_sensor(self, sensorobj):
        self.splist.append(sensorobj)

# I would put this method in both the Drone and Rover class
# because it uses the inbox attribute to recive the message.
# There is no need for all the classes to inherit this method
# since there are only two classes which will actually use it.

def send_msg_to_robot_operators(self, msg):
    send = ("Message from Site Manager:\n" + msg)
    self.inbox.append(send)


aqd = AirQualityDrone()

site_manager = SiteManager()
