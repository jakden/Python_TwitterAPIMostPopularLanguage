
import json
import pandas as pd
import matplotlib.pyplot as plt

tweets_data_path = 'C:/Python34/Scripts/Python_TwitterAPIMostPopularLanguage/twitterdata.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
dict1 = tweets_data[1]
if 'lang' in dict1:
  print("blah")
else:
  print("boo")


"""tweets_dataSearchable = (tweets_data[1]).lower()
termRequest = input('What keyword are you looking for: ' ).lower()

termSearched = ([s for s in tweet_dataSearchable if termRequest in s])

if termSearched == "":
	print(termSearched)
	print('No text found')

if termSearched == terSearched:
	print(termSearched).count()"""










