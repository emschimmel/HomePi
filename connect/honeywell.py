import ConfigParser

class Honeywell():
    config = ConfigParser.RawConfigParser()
    config.read('config/config.properties')

    print config.get('Honeywell', 'consumer_key')

    def send(self, command):
        print("TODO", command)