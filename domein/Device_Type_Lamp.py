from domein.Device_Type import DeviceType
from domein.Device import Device
from connect import pylightwaverf

class Device_Type_Lamp(Device):
    typedevice = DeviceType.LAMP

    STATE_OFF  = '0'
    STATE_ON   = '1'
    STATE_DIM  = 'dP'
    STATE_LOW  = 'dP8'
    STATE_MED  = 'dP16'
    STATE_HIGH = 'dP24'
    STATES = {
        STATE_OFF  : 'F0',
        STATE_ON   : 'F1',
        STATE_DIM  : 'FdP',
        STATE_LOW  : 'FdP8',
        STATE_MED  : 'FdP16',
        STATE_HIGH : 'FdP24',
    }

    def _send_command(self, command):
        room   = self.room
        device = self.device
        print("command", command)
        pylightwaverf.LightWaveRF().control(room, device, command)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        if 0 <= state <= 100:
            command = 'FdP' + str(int(state * 0.32))
        elif Device_Type_Lamp.STATES.get(state):
            command = Device_Type_Lamp.STATES.get(state)
        else:
            raise Exception('State not recognised')
        self._send_command(command)
        self._state = state

    def pair(self):
        '''
        Call this once device is in pairing mode to pair the device
        '''
        self.state = Device_Type_Lamp.STATE_ON

    def sendValueToLamp(self, val, slider):
        slider.set(val)

    def sendValueToLampBySlider(self, val):
        self._send_command(self.createComand(val))

    def sendValueLampOff(self, slider):
        slider.set(0)
        self._send_command(Device_Type_Lamp.STATE_OFF)

    def sendValueLampOn(self, slider):
        slider.set(100)
        self._send_command(Device_Type_Lamp.STATE_ON)

    def createComand(self, val):
        kaku_val = (int(val)/3)-1
        if kaku_val <1:
            command = Device_Type_Lamp.STATE_OFF
        else:
            command = Device_Type_Lamp.STATE_DIM+`kaku_val`
        return command