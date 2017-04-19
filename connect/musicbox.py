import ConfigParser

class MusicBox():
    config = ConfigParser.RawConfigParser()
    config.read('config/config.properties')

#    print config.get('MusicBox', 'key')

    def send(self, command):
        print("TODO", command)
