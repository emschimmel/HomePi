import Device as device
import Room as room

class RoomCollection():

    SELECTEDROOM_DEFAULTVALUE = {'name' : 'Hallway', 'roomConfigCollection' : []}
    ROOMCOLLECTION = [[{'name' : 'Livingroom', 'roomConfigCollection' : [device.Device(1, 1, "lamp", "Lamp"), device.Device(1, 2, "lamp", "StaLamp")]}], [{'name' : 'Bedroom', 'roomConfigCollection' : [device.Device(2, 1, "lamp", "Lamp")]}, {'name' : 'Library', 'roomConfigCollection' : [device.Device(3, 1, "lamp", "Lamp")]}, {'name' : 'Childroom', 'roomConfigCollection' : [device.Device(4, 1, "lamp", "MooiLamp")]}]]

    def __init__(self):
        self._build_collection()

    @property
    def state(self):
        return self._state


    def _build_collection(self):
        self.ROOMCOLLECTION   = self.ROOMCOLLECTION

