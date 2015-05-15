
import json
import collections
from collections import Counter


tweets_data_path = 'C:/Python34/Scripts/twitter/twitterdata.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

while_max = len(tweets_data)
while_max = int(while_max)

y = 0
full_text = []
failed_text = 0

while y != 100: #whileloop to run through all tweets in the file
  y += 1
  try:
    textoftweet = tweets_data[y]['text']
    textoftweet = textoftweet.encode("utf-8", errors='ignore')
    full_text.append(textoftweet)
  except:
      print('failed to decypher and append')

    
full_text.append(textoftweet)
#full_encoded_text = full_text.encode("utf-8", errors='ignore')
print(full_text)





while_max = len(tweets_data)
while_max = int(while_max)
print(type(while_max))
print(while_max) #prints max number of tweets in the list

#tried twitter_param = input('which twitter parameter would you like to search for?') but will not work for other parms
x = 0
full_dict = []
failed_dict = 0

while x != while_max: #whileloop to run through all tweets in the file
  x += 1
  try:
    dict_1 = tweets_data[x]['lang'] #creates an object to be appended to a list of all languages
    
    full_dict.append(dict_1)
  except: #exception for no language given
    failed_dict += 1
    
    
print( failed_dict, 'tweets do not have an assigned language')    
print(Counter(full_dict)) #counts and displays the number of tweets from each language











