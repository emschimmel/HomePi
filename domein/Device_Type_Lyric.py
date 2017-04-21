from domein.Device_Type import DeviceType
from domein.Device import Device
from connect.honeywell import Honeywell

import threading

class Device_Type_Lyric(Device):
    typedevice = DeviceType.LYRIC
    current_temperature = 0
    running_update = False

    ### Location == room
    def get_temperature(self):
        if not self.running_update:
            self.update_temperature()
        return self.current_temperature

    ### Timed thread to get the temperature
    def update_temperature(self):
        self.running_update = True
        #threading.Timer(60.0, self.update_temperature).start()
        self.current_temperature = Honeywell().get_temperature(self.device)
        print(self.current_temperature)

    def _send_command(self, command):
        return Honeywell().send(command)


