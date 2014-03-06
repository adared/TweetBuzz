from twython import Twython
from twython import TwythonStreamer
from repoze.lru import lru_cache

class TrendFinder(object):
	def __init__(self, creds):
		self.api = Twython(**creds)

	@lru_cache(maxsize=500, timeout=15*60)
	def find_trends(self):
		trend_response = self.api.get_place_trends(id=23424977)
		trends = {}
		for trend in trend_response[0]["trends"]:
			name = trend["name"]
			trends[name] = self.get_tweets_for_trend(name)
		return trends
	
	@lru_cache(maxsize=500, timeout=15*60)
	def get_tweets_for_trend(self, trend):
		tweet_response = self.api.search(q=trend)
		print tweet_response
		trend_tweets = []
		for tweet in tweet_response['statuses']:
			trend_tweets.append(dict(
				name=tweet["user"]['name'],
				tweet=tweet['text']))
		return trend_tweets