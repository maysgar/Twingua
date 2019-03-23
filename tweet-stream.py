import tweepy
import sys
import time
import os

# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")
CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")

# print(os.environ.get('CONSUMER_KEY'))
# print(os.environ)

# output_file = 'tweets_eu.json'
output_file2 = 'tweets_eu_3.json'

# Mapbox done at http://boundingbox.klokantech.com/
GEO_EUROPE_BOX = [-24.64501397,35.8630349534,45.1656662867,71.2702519386]

# Languages in Europe
LANGUAGES = ["es, en, cs, da, de, el, fi, fr, he, hu, it, nl, no, pl, pt, ro, ru, sv, tr, uk"]

# initialize a list to hold all the tweepy Tweets
alltweets = []


# Stream listener
class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print status.text

    # Write the tweets on the JSON file
    def on_data(self, data):
        # if file is bigger than 90 MB exit the program
        if os.path.getsize(output_file2) > 90000000:
            print "File is ", os.path.getsize(output_file2), ". Bigger than 90MB, exiting the program"
            exit()
        file.write(data)

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

# authenticate access to Twitter API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
# open output file of the downloaded tweets
file = open(output_file2, 'a')

# Error handling
if not api:
    print ("Problem connecting to API")

# myStreamListener = MyStreamListener()
# myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

print("Starting Streaming filter")

# Start Streaming filter
stream = tweepy.streaming.Stream(auth, CustomStreamListener())

# filter tweets by set of languages and boundary box around Europe
stream.filter(languages=LANGUAGES, locations=GEO_EUROPE_BOX)

# Let the program sleep if we reach the maximum number of requests
time.sleep(10)

print("Done with the filtering")

# new_tweets = myStream.filter(languages=LANGUAGES, locations=GEO_EUROPE_BOX, count=["10"])
# print(json.dumps(myStream.filter(locations=GEO_EUROPE_BOX)))

'''
for tweet in new_tweets:

        # add to JSON
        counter += 1
        print ("Counter: ",counter,"tweets")
        with open('tweets_eu.json', 'w', encoding='utf8') as file:
            json.dump(tweet._json, file)
'''