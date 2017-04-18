import Device as device
import Room as room

class RoomCollection():

    SELECTEDROOM_DEFAULTVALUE = room.Room('Hallway', [])
    ROOMCOLLECTION = [[room.Room('Livingroom', [device.Device(1, 1, "lamp", "Lamp"), device.Device(1, 2, "lamp", "StaLamp")])], [room.Room('Bedroom', [device.Device(2, 1, "lamp", "Lamp")]), room.Room('Library', [device.Device(3, 1, "lamp", "Lamp")]), room.Room('Childroom', [device.Device(4, 1, "lamp", "MooiLamp")])]]

    def __init__(self):
        self._build_collection()

    @property
    def state(self):
        return self._state


    def _build_collection(self):
        self.ROOMCOLLECTION   = self.ROOMCOLLECTION

