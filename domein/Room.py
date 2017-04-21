

class Room:
    def __init__(self, name, device_collection):
        self.number  = 1
        self.name    = name
        self.deviceCollection  = device_collection
        self.moods   = []

#    def add_device(self, device):
#        if device.__class__ is not Device:
#            raise Exception('device: %s is not a Device' % device)
#        self.devices.append(device)
