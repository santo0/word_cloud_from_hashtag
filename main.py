import GetOldTweets3 as got
import pandas as pd

NUMBER_OF_TWEETS = 10

result_dict = {}

def get_tweets(input_hashtag):
    input_hashtag = list(input_hashtag.split(","))
    for i in range(len(input_hashtag)):
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(input_hashtag[i]).setMaxTweets(NUMBER_OF_TWEETS)
        tweet_bodies = []
        for j in range(NUMBER_OF_TWEETS):
            tweet = got.manager.TweetManager.getTweets(tweetCriteria)[j]
            date_time = tweet.date.strftime("%d/%m/%Y, %H:%M:%S")
            tweet_bodies.append((tweet.text,date_time))
        result_dict[input_hashtag[i]] = tweet_bodies

    return result_dict



