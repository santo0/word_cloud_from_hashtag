import GetOldTweets3 as got
from word_cloud import get_stop_words_by_language, get_filtered_text, draw_word_cloud
from tweet_fetcher import get_tweets
import timeit

def run(input_hashtag):
    tweet_dict = get_tweets([hashtag.strip() for hashtag in input_hashtag.split(",")])
    full_text = ""
    for hashtag in tweet_dict:
        for tweet in tweet_dict[hashtag]:
            print(tweet)
            full_text += get_filtered_text(tweet[0], "spanish")
    draw_word_cloud(full_text)



