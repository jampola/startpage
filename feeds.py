import feedparser
import pprint

# feed_url = "https://www.reddit.com/r/news/.rss"
feed_url = "https://news.google.com/news?cf=all&hl=en&pz=1&ned=us&output=rss"

d = feedparser.parse(feed_url)

html_news=""
for x in range(1,10):
	html_news+="<a href={}>{}</a>".format(d['entries'][x]['links'][0]['href'],d['entries'][x]['title'])
print html_news