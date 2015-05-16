
import json
import collections
from collections import Counter
import re


tweets_data_path = 'C:/Python34/Scripts/Python_TwitterAPISearch/twitterdata.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")

for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue



print('param options are:\n' 'text - gives you all text from all tweets in .txt\n'
      'lang - gives you a count for how many tweets appear in different languages from tweets in .txt')
#
search_param = input('which search param do you want? ')

if search_param == 'text':
  search_tweets = (input('What word would you like to search for? '))

while_max = len(tweets_data)
while_max = int(while_max)

y = 0
full_text = []
failed_text = 0
failed_lang = 0

id_of_tweet = []

while y != while_max: #whileloop to run through all tweets in the file
  y += 1

  try:
    text_of_tweet = tweets_data[y][search_param]
    id_of_tweet = tweets_data[y]['id_str']
    full_text.append(text_of_tweet)

    if search_tweets in text_of_tweet:
      #print(aa)
      #print(bb)
      print(id_of_tweet)
      print(text_of_tweet)
      print('')
      
  except:
    if search_param == 'text':
      failed_text += 1

    if search_param ==  'lang':
      failed_lang += 1  

if search_param == 'lang':
  print(Counter(full_text))
  print(failed_lang, 'tweets do not have an assigned language') 
if search_param == 'text':
  print(failed_text, 'failed to decypher and append')
#.encode("utf-8", errors='ignore')
#add sender of tweet
#link to their page???






#ids = []
#for tweet in tweets:
    #if 'id_str' in tweet:
        #ids.append(tweet['id_str'])