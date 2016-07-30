
from instagram.client import InstagramAPI

access_token = "2299001890.beae370.abcb56ac503f4bcbb6f3f23a0da586f9"
client_secret = "c1f9b80396084bed83818a571e6521d8"
api = InstagramAPI(access_token=access_token, client_secret=client_secret)
recent_media, next_ = api.user_recent_media(user_id="userid", count=10)
for media in recent_media:
   print media.caption.text
