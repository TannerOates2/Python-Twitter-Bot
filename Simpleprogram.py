from twython import Twython

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

#opens the file and read it
with open("scraped_text.txt", 'r') as myfile:

#reads file and puts in variable
    data = myfile.read().replace('\n', '')

#updates twitter status
twitter.update_status(status=data)

#prints the text in the file
print("Tweeted: {}".format(data))
