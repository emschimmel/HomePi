import pylightwaverf
kaku = pylightwaverf.LightWaveRF()

class Device():

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

    def __init__(self, room, device, typedevice, name=None, state=None):
        self.room    = room
        self.device  = device
        self.name    = name
        self.typedevice    = typedevice
        self._state  = state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        if 0 <= state <= 100:
            command = 'FdP' + str(int(state * 0.32))
        elif STATES.get(state):
            command = STATES.get(state)
        else:
            raise Exception('State not recognised')
        self._send_command(command)
        self._state = state

    def pair(self):
        '''
        Call this once device is in pairing mode to pair the device
        '''
        self.state = STATE_ON

    def _send_command(self, command):
        room   = self.room
        device = self.device
        print("command", command)
        kaku.control(room, device, command)

    def sendValueToLamp(self, val, slider):
        slider.set(val)

    def sendValueToLampBySlider(self, val):
        self._send_command(self.createComand(val))

    def sendValueLampOff(self, slider):
        slider.set(0)
        self._send_command(Device.STATE_OFF)

    def sendValueLampOn(self, slider):
        slider.set(100)
        self._send_command(Device.STATE_ON)

    def createComand(self, val):
        kaku_val = (int(val)/3)-1
        if kaku_val <1:
            command = Device.STATE_OFF
        else:
            command = Device.STATE_DIM+`kaku_val`
        return command