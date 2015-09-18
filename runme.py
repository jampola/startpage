# -*- coding: utf-8 -*-
#!/usr/bin/python2

import html_content
import weather
import rssfeeds

# this is a bunch of code that generates my start page and 
# updating some use(less)ful info such as weather and RSS feeds
# that I will probably never click on.
# html_content containing the dictionary of html links I want populated
# weather is the weather code pulling data using the yahoo API
# rssfeeds is pulling the rss data from google news.
# jb (at) jamesbos (dot) com

class startPageWriter:
	def __init__(self,feed_url,weather_woeid,html_template_file,html_output_file):
		self.feed_url = feed_url
		self.weather_woeid = weather_woeid
		self.html_template_file = html_template_file
		self.html_output_file = html_output_file
		self.weather_data = weather.weatherData(self.weather_woeid)
		self.rss_builder = rssfeeds.rssFeeds(self.feed_url)

	def list_builder(self,linkdict):
		links_build=""
		for key,val in linkdict.iteritems():
			links_build+="    <li><a href='%s'>%s</a></li>\n"	% (val,key)
		built_html = "%s %s %s" % ("<ul>\n",links_build,"</ul>")
		return built_html

	def run(self):
		news_links_html = self.list_builder(html_content.news_links)
		reddit_links_html = self.list_builder(html_content.reddit_links)
		social_links_html = self.list_builder(html_content.social_links)

		in_file = open(self.html_template_file,"r").read()

		output = ""

		output = in_file.replace("$news_links",news_links_html)
		output = output.replace("$reddit_links",reddit_links_html)
		output = output.replace("$social_links",social_links_html)
		output = output.replace("$weather_data",self.weather_data.run())
		output = output.replace("$rss_data",self.rss_builder.run())

		print output

		f_out = open(self.html_output_file,"w")
		f_out.write(output)
		f_out.close()

if __name__ == '__main__':
	# fill in relevant fields here.
	feed_url = "https://news.google.com/news?cf=all&hl=en&pz=1&ned=us&output=rss"
	weather_woeid = "1226059"
	html_template_file='/home/james/startpage/template.html'
	html_output_file='/home/james/startpage/start.html'
	
	app = startPageWriter(feed_url, weather_woeid, html_template_file, html_output_file)
	app.run()