from domein.Device_Type import DeviceType
from domein.Device import Device
from connect.honeywell import Honeywell

class Device_Type_Lyric(Device):
    typedevice = DeviceType.LYRIC

    def _send_command(self, command):
        Honeywell.send(self.command)
