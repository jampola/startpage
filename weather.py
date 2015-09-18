# -*- coding: utf-8 -*-
#!/usr/bin/python
import urllib2
import json
import time
import os
import sys
import pprint

class weatherData:
	def __init__(self,woeid):
		self.user_woeid = woeid

	def get(self,woeid,unit_format):
		
		q='SELECT%20*%20FROM%20weather.forecast%20WHERE%20woeid="{}"%20and%20u="{}"&format=json'.format(woeid,unit_format)
		weather_req_url = 'http://query.yahooapis.com/v1/public/yql?q={}'.format(q)
		request = urllib2.urlopen(weather_req_url).read()
		self.data = json.loads(request)
		# pprint.pprint(self.data)
		
		self.title = self.data['query']['results']['channel']['item']['title']
		self.desc = self.data['query']['results']['channel']['description'][7:]
		self.last_update = self.data['query']['results']['channel']['lastBuildDate']

		# current conditions
		self.current_temp = self.data['query']['results']['channel']['item']['condition']['temp']
		self.current_conditions = self.data['query']['results']['channel']['item']['condition']['text']
		self.humidity = self.data['query']['results']['channel']['atmosphere']['humidity']
		
		# forecast for the next 4 days
		self.current_forcast_min_temp_day0 = self.data['query']['results']['channel']['item']['forecast'][0]['low']
		self.current_forcast_max_temp_day0 = self.data['query']['results']['channel']['item']['forecast'][0]['high']
		self.current_forcast_date_day0 = self.data['query']['results']['channel']['item']['forecast'][0]['date']
		self.current_forcast_day_day0 = self.data['query']['results']['channel']['item']['forecast'][0]['day']
		self.current_forcast_text_day0 = self.data['query']['results']['channel']['item']['forecast'][0]['text']

		self.current_forcast_min_temp_day1 = self.data['query']['results']['channel']['item']['forecast'][1]['low']
		self.current_forcast_max_temp_day1 = self.data['query']['results']['channel']['item']['forecast'][1]['high']
		self.current_forcast_date_day1 = self.data['query']['results']['channel']['item']['forecast'][1]['date']
		self.current_forcast_day_day1 = self.data['query']['results']['channel']['item']['forecast'][1]['day']
		self.current_forcast_text_day1 = self.data['query']['results']['channel']['item']['forecast'][1]['text']

		self.current_forcast_min_temp_day2 = self.data['query']['results']['channel']['item']['forecast'][2]['low']
		self.current_forcast_max_temp_day2 = self.data['query']['results']['channel']['item']['forecast'][2]['high']
		self.current_forcast_date_day2 = self.data['query']['results']['channel']['item']['forecast'][2]['date']
		self.current_forcast_day_day2 = self.data['query']['results']['channel']['item']['forecast'][2]['day']
		self.current_forcast_text_day2 = self.data['query']['results']['channel']['item']['forecast'][2]['text']

		self.current_forcast_min_temp_day3 = self.data['query']['results']['channel']['item']['forecast'][3]['low']
		self.current_forcast_max_temp_day3 = self.data['query']['results']['channel']['item']['forecast'][3]['high']
		self.current_forcast_date_day3 = self.data['query']['results']['channel']['item']['forecast'][3]['date']
		self.current_forcast_day_day3 = self.data['query']['results']['channel']['item']['forecast'][3]['day']
		self.current_forcast_text_day3 = self.data['query']['results']['channel']['item']['forecast'][3]['text']

		self.current_forcast_min_temp_day4 = self.data['query']['results']['channel']['item']['forecast'][4]['low']
		self.current_forcast_max_temp_day4 = self.data['query']['results']['channel']['item']['forecast'][4]['high']
		self.current_forcast_date_day4 = self.data['query']['results']['channel']['item']['forecast'][4]['date']
		self.current_forcast_day_day4 = self.data['query']['results']['channel']['item']['forecast'][4]['day']
		self.current_forcast_text_day4 = self.data['query']['results']['channel']['item']['forecast'][4]['text']

		# sunrise and set
		self.sunrise = self.data['query']['results']['channel']['astronomy']['sunrise']
		self.sunset = self.data['query']['results']['channel']['astronomy']['sunset']

		# location info
		self.city = self.data['query']['results']['channel']['location']['city']
		self.country = self.data['query']['results']['channel']['location']['country']

		html_current_conditions = "Temp {}&deg;, Humidity {}% and {}".format(self.current_temp,\
			self.humidity,self.current_conditions)

		html_astonomy = "Sunrise: {} Sunset: {}".format(self.sunrise,self.sunset)

		html_forecasy_day0 = "{},{} Low: {} High: {} & {}".format(self.current_forcast_day_day0,self.current_forcast_date_day0,\
			self.current_forcast_min_temp_day0,self.current_forcast_max_temp_day0, self.current_forcast_text_day0)
		html_forecasy_day1 = "{},{} Low: {} High: {} & {}".format(self.current_forcast_day_day1,self.current_forcast_date_day1,\
			self.current_forcast_min_temp_day1,self.current_forcast_max_temp_day1, self.current_forcast_text_day1)
		html_forecasy_day2 = "{},{} Low: {} High: {} & {}".format(self.current_forcast_day_day2,self.current_forcast_date_day2,\
			self.current_forcast_min_temp_day2,self.current_forcast_max_temp_day2, self.current_forcast_text_day2)
		html_forecasy_day3 = "{},{} Low: {} High: {} & {}".format(self.current_forcast_day_day3,self.current_forcast_date_day3,\
			self.current_forcast_min_temp_day3,self.current_forcast_max_temp_day3, self.current_forcast_text_day3)
		html_forecasy_day4 = "{},{} Low: {} High: {} & {}".format(self.current_forcast_day_day4,self.current_forcast_date_day4,\
			self.current_forcast_min_temp_day4,self.current_forcast_max_temp_day4, self.current_forcast_text_day4)

		html_build = "\
		<h2>Current Conditions ({}, {})</h2>\
		<span>{}</span><br>\
		<h2>Astronomy</h2>\
		<span>{}</span><br>\
		<h2>Outlook</h2>\
		<span>{}</span><br>\
		<span>{}</span><br>\
		<span>{}</span><br>\
		<span>{}</span><br>\
		<span>{}</span><br>\
		<span class='footer'>Weather Last Updated: {}</span>".format(self.city,self.country,html_current_conditions,html_astonomy,html_forecasy_day0,html_forecasy_day1,html_forecasy_day2,html_forecasy_day3,\
			html_forecasy_day4,self.last_update)

		return html_build

	def run(self):
		return self.get(self.user_woeid,'c')

if __name__ == '__main__':
	# testing within class.
	app = weatherData('1226059')
	app.run()
