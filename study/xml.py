#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from pyexpat import ParserCreate
from urllib import request


def parseXml(xml_str):
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)
    return handler.cityweather.__dict__()


class CityWeather(object):

    def __init__(self):
        self.city = None
        self.forecast = []

    def __getcityweatherforecast(self):
        cityweatherforecast = {}
        cityweatherforecast['city'] = self.city
        cityweatherforecast['forecast'] = [
            {'date': weatherforecast.date, 'day': weatherforecast.day,
             'high_tem': weatherforecast.high_tem, 'low_tem': weatherforecast.low_tem,
             'weather': weatherforecast.weather} for weatherforecast in
            self.forecast]
        return cityweatherforecast

    def __dict__(self):
        return self.__getcityweatherforecast()


class Forecast(object):
    __slots__ = ('date', 'day', 'high_tem', 'low_tem', 'weather')

    weekday = {
        'Mon': '一',
        'Tue': '二',
        'Wed': '三',
        'Thu': '四',
        'Fri': '五',
        'Sat': '六',
        'Sun': '日',
    }
    month = {
        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'Aug': 8,
        'Sep': 9,
        'Oct': 10,
        'Nov': 11,
        'Dec': 12
    }

    def __init__(self, date, day, high_tem, low_tem, weather):
        self.date = date
        self.day = day
        self.high_tem = high_tem
        self.low_tem = low_tem
        self.weather = weather


class WeatherSaxHandler(object):

    @property
    def cityweather(self):
        return self.__cityweather

    def start_element(self, name, attrs):
        if name == 'channel':
            self.__cityweather = CityWeather()
        self.__nodename = name
        self.__nodenameattrs = attrs

    def end_element(self, name):
        if name == 'yweather:location':
            self.__cityweather.city = self.__nodenameattrs['city']
        if name == 'yweather:forecast':
            def forecastformat(attrs):
                date = re.split(r'\s+', attrs['date'])[::-1]
                date[1] = Forecast.month[date[1]]
                date = '-'.join([str(int(n)) for n in date])
                day = '星期%s' % (Forecast.weekday[attrs['day']])
                heigh_tem = '%.1f ºC' % ((float(attrs['high']) - 32) / 1.8)
                low_tem = '%.1f ºC' % ((float(attrs['low']) - 32) / 1.8)
                weather = attrs['text']
                return date, day, heigh_tem, low_tem, weather

            forecast = Forecast(*forecastformat(self.__nodenameattrs))
            self.__cityweather.forecast.append(forecast)

    def char_data(self, text):
        return


# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=2) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
print(result)
assert result['city'] == 'Beijing'
print('ok')
