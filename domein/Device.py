

class Device():

    def __init__(self, room, device, name=None):
        self.room    = room
        self.device  = device
        self.name    = name

#### example for implementable function
    def _send_command(self, command):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

