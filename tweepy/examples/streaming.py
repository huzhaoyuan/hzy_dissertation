from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key = 'bSqMiPXiVElmhBIThndjHA39B'
consumer_secret = 'AlmcT9t1kVNABkDxRheNBRQDwkLRbM3VdJF84kfIUASeikQQge'
access_token = '4312482747-cmIdm2pK5no2HNB7a0BfrMwXTIqlRaM6MOAlfNh'
access_token_secret = 'iqAnAilsX9vgXrfC5XXtg41o49ppeOKCzcifDTWxKgjj6'

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token = '4312482747-cmIdm2pK5no2HNB7a0BfrMwXTIqlRaM6MOAlfNh'
access_token_secret = 'iqAnAilsX9vgXrfC5XXtg41o49ppeOKCzcifDTWxKgjj6'

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        with open('result.txt','a+') as tf:
            tf.write(data)
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['#fitness'])

