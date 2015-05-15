
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

while_max = len(tweets_data)
while_max = int(while_max)

y = 0
full_text = []
failed_text = 0
failed_lang = 0

while y != while_max: #whileloop to run through all tweets in the file
  y += 1
  try:
    textoftweet = tweets_data[y][search_param]
   # textoftweet = textoftweet.encode("utf-8", errors='ignore')
    full_text.append(textoftweet)
  except:
    if search_param == 'text':
      print('failed to decypher and append')
    if search_param ==  'lang':
      failed_lang += 1  

#if search_param == 'id':
 # print(full_text)
#if search_param == 'text':  #removed this  ---- .encode("utf-8", errors='ignore') needs to be done at the end of your search
  #print(full_text)
if search_param == 'lang':
  print(Counter(full_text))
  for i in Counter(full_text):
    print(i)
  print( failed_lang, 'tweets do not have an assigned language')  


#Search full text for a specific word
#display those tweets with the word associated with them

search_tweets = (input('What word would you like to search for? '))
#full_list -> search_tweets is the word
if any(search_tweets in s for s in full_text):  
  print('There are results')
search_tweets = ([s for s in full_text if search_tweets in s])
#search_tweets is a list
#SPLIT ALL OF THESE TO DISPLAY IN A ROW
#NEEDS TO BE DONE BY RUNNING EACH ITEM THROUGH STEPS RATHER THAN WHOLE LIST

search_tweet_string = ''.join(search_tweets)
print(type(search_tweet_string))
print(search_tweet_string.encode("utf-8", errors='ignore'))
  

#split list eash word
#contains attribute








