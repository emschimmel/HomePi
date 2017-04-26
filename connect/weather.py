# https://pypi.python.org/pypi/pywapi

#!/usr/bin/env python
#import pywapi
#import string

# yahoo_result = pywapi.get_weather_from_yahoo('10001')
#noaa_result = pywapi.get_weather_from_noaa('KJFK')
# NLXX0053

#locale = pywapi.get_loc_id_from_weather_com('Almere Stad')
#print locale

# print "Yahoo says: It is " + string.lower(yahoo_result['condition']['text']) + " and " + yahoo_result['condition']['temp'] + "C now in New York.\n\n"

#print "NOAA says: It is " + string.lower(noaa_result['weather']) + " and " + noaa_result['temp_c'] + "C now in New York.\n"

#----------------------
# Next
#----------------------
import logging
import ConfigParser
from yahooweather import YahooWeather, UNIT_C, get_woeid

class weather():

    config = ConfigParser.RawConfigParser()
    config.read('config/config.properties')

    # LAT = config.get('Weather', 'latitude')
    # LANG = config.get('Weather', 'langitude')
    LAT		=	52.3504550
    LANG		=	5.1511460

    print("The woeid from Gstaad is: %s" % get_woeid(LAT, LANG))


    logging.basicConfig(level=logging.WARNING)
    yweather = YahooWeather(get_woeid(LAT, LANG), UNIT_C)


    def __init__(self):
        if self.yweather.updateWeather():
        #    print("RawData: %s" % str(yweather.RawData))
        #    print("----------------------")
        #    print("Units: %s" % str(yweather.Units))
        #    print("----------------------")
            WEATHER_NOW = self.yweather.Now
        #    print("Now: %s" % str(self.yweather.Now))
        #    print("----------------------")
            WEATHER_FORECAST = self.yweather.Forecast
            print("Forecast: %s" % str(self.yweather.Forecast))
            print("----------------------")
            WEATHER_WIND = self.yweather.Wind
            print("Wind: %s" % str(self.yweather.Wind))
            print("----------------------")
            WEATHER_ATMOSPHERE = self.yweather.Atmosphere
            print("Atmosphere: %s" % str(self.yweather.Atmosphere))
            print("----------------------")
            WEATHER_ASTRONOMY = self.yweather.Astronomy
            print("Astronomy: %s" % str(self.yweather.Astronomy))
            print("----------------------")
            WEATHER_ICON = self.yweather.getWeatherImage(WEATHER_NOW["code"])
            print("Weather image from current: %s" %
                  self.yweather.getWeatherImage(WEATHER_NOW["code"]))

            print("The woeid from Gstaad is: %s" % get_woeid(self.LAT, self.LANG))
        else:
            print("Can't read data from yahoo!")