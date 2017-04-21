import ConfigParser
from connect.httpConnectWithOauth import httpConnectWithOauth

#--------------------------------------------------------
# getAutorisation -> get OAuth token
# get devices result
#   - indoorTemperature
#   - outdoorTemperature
#   - units
#   - changeableValues
#           - heatSetpoint
#--------------------------------------------------------
class Honeywell:
    config = ConfigParser.RawConfigParser()
    config.read('config/config.properties')


    def __init__(self):
        self.apikey = self.config.get('Honeywell', 'consumer_key')
        self.get_acces()

    def get_acces(self):
        url = self.config.get('Honeywell-urls', 'authorize')
        httpConnectWithOauth().getAcces(url, self.apikey)

    def get_temperature(self, device):
        url = self.config.get('Honeywell-urls', 'termostate')
        #return "21"
        return httpConnectWithOauth().getWithValues(url, self.apikey, device)

    def send(self, command):
        print("TODO", command)

    def get_deviceid(self):
        self.config.get('Honeywell', 'deviceid')

    def get_locationid(self):
        self.config.get('Honeywell', 'locationid')

