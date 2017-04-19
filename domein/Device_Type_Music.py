from domein.Device_Type import DeviceType
from domein.Device import Device
from connect.musicbox import MusicBox

class Device_Type_Music(Device):
    typedevice = DeviceType.MUSIC

    def _send_command(self, command):
        MusicBox.send(self.command)
