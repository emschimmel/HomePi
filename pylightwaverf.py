import socket
import re

# werkend commando:
# echo -ne '100,!F*p' | nc -u 192.168.0.102 9760

class LightWaveRF():

    SOCKET_TIMEOUT = 2.0
    RX_PORT        = 9761
    TX_PORT        = 9760
    WTF            = '0,' # No clue why, with this added it worked...

    def __init__(self):

        # Set up transmission socket (allow broadcasting)
        tx_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        tx_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        tx_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tx_sock.settimeout(self.SOCKET_TIMEOUT)
        self.tx_sock = tx_sock

        # Set up receive socket
        rx_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        tx_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        rx_sock.settimeout(self.SOCKET_TIMEOUT)
        rx_sock.bind(('0.0.0.0', self.RX_PORT))
        self.rx_sock = rx_sock

        # Set the initial msg_id
        self.msg_id = 1

        # Find the WiFiLink
        self.wifilink_ip = "192.168.0.102"
        #self.wifilink_ip = self.locate_wifilink()


    def locate_wifilink(self):
        msg_data = self.WTF+'@?v'
        try:
            data, ip = self.send(msg_data, broadcast=False)
            print(data)
        except socket.timeout:
            print(socket.timeout)
            return None
        print(data)
        valid    = re.compile(r'^\d{1,3},\?V=(.*)\r\n$')
        match    = valid.match(data)
        if match:
            return ip
        return None

    def register_device(self):
        msg_data = self.WTF+'!F*p'
        data, ip = self.send(msg_data)
        print(data)
        print(ip)

    def get_power(self):
        msg_data = self.WTF+'@?W'
        data, ip = self.send(msg_data)
        valid    = re.compile(r'^\d{1,3},\?W=([0-9,]+)\r\n$')
        match    = valid.match(data)
        if match:
            power = match.group(1).split(',')
            return {
                'current':         power[0],
                'max_today':       power[1],
                'total_today':     power[2],
                'total_yesterday': power[3],
            }
        return None


    def control(self, room=None, device=None, state=None, msg1=None, msg2=None):
        room   = 'R%d' % room   if room   is not None else ''
        device = 'D%d' % device if device is not None else ''
        state  = 'F%s' % state  if state  is not None else ''

        command  =  ''.join([self.WTF, '!', room, device, state])
        msg_data = '|'.join(filter(None,[command, msg1, msg2]))
        self.send(msg_data)

    def test_control(self, val):
        msg_data = self.WTF+'!R1D1FdP'+`val`
        print("msg_data", msg_data)
        self.send(msg_data)


    def send(self, msg_data, broadcast=False):
        data = self.get_next_msg_id() + msg_data
        if broadcast:
            ip = '255.255.255.255'
        else:
            ip = self.wifilink_ip
        self.tx_sock.sendto(data, (ip, self.TX_PORT))

        data, addr = self.rx_sock.recvfrom(1024)
        ip, port   = addr

        return (data, ip)


    def get_next_msg_id(self):
        # Ensure we always generate msg_ids from 001-999
        msg_id = self.msg_id + 1
        if msg_id % 1000 == 0:
            msg_id = 1
        self.msg_id = msg_id
        return '%03d' % msg_id


class Room():

    def __init__(self, number):
        self.number  = number
        self.name    = None
        self.devices = []
        self.moods   = []

    def add_device(self, device):
        if device.__class__ is not Device:
            raise Exception('device: %s is not a Device' % device)
        self.devices.append(device)


class Device():

    STATE_OFF  = 'OFF'
    STATE_ON   = 'ON'
    STATE_LOW  = 'LOW'
    STATE_MED  = 'MED'
    STATE_HIGH = 'HIGH'
    STATES = {
        STATE_OFF  : 'F0',
        STATE_ON   : 'F1',
        STATE_LOW  : 'FdP8',
        STATE_MED  : 'FdP16',
        STATE_HIGH : 'FdP24',
    }

    def __init__(self, room, number, name=None, state=None):
        self.room    = room
        self.number  = number
        self.name    = name
        self.type    = type
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
        room   = self.room.number
        device = self.number
        msg    = room + device + command
    #TODO: Send command
