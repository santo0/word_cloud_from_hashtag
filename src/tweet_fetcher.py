import GetOldTweets3 as got
from word_cloud import get_stop_words_by_language, get_filtered_text, draw_word_cloud
from dec_timer import timer
import time
NUMBER_OF_TWEETS = 100

@timer
def get_tweets(input_hashtag):
    result_dict = {}
    for i in range(len(input_hashtag)):
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(
            input_hashtag[i]).setMaxTweets(NUMBER_OF_TWEETS)
        tweet_bodies = []
        for j in range(NUMBER_OF_TWEETS):
            start_time = time.time()
            tweet = got.manager.TweetManager.getTweets(tweetCriteria)[j]
            date_time = tweet.date.strftime("%d/%m/%Y, %H:%M:%S")
            end_time = time.time() -start_time
            print('Finished {} in {:.2f} secs'.format(j, end_time))
            tweet_bodies.append((tweet.text, date_time))
        result_dict[input_hashtag[i]] = tweet_bodies
    return result_dict
