# -*- coding: utf-8 -*-
#!/usr/bin/python
# This probably only works well with Google News feeds so YMMV.
# For any other news feeds, import pprint and pprint the feed
# to find the dict keys.
import feedparser

class rssFeeds:
	def __init__(self,rssurl):
		self.rssurl = rssurl

	def run(self):
		d = feedparser.parse(self.rssurl)
		html_news=""
		for x in range(1,10):
			news_url = d['entries'][x]['links'][0]['href']
			news_title = d['entries'][x]['title']
			news_title = news_title.encode('utf-8')
			if len(news_title) > 63:
				news_title=news_title[0:63]+"...."
			if x % 2 == 0:
				html_news+="<li class='even'><a href={}>{}</a></li>".format(news_url,news_title)
			else:
				html_news+="<li class='odd'><a href={}>{}</a></li>".format(news_url,news_title)
		return html_news		
		# print html_news		

if __name__ == '__main__':
	# testing within class.
	app = rssFeeds('https://news.google.com/news?cf=all&hl=en&pz=1&ned=us&output=rss')
	app.run()
