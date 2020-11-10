#!/usr/bin/env python
# coding: utf-8

# ### Import Libraries

# In[1]:


# importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
# import joblib
from joblib import dump
# import joblib
from joblib import load

from wordcloud import WordCloud
import re
from nltk.corpus import stopwords
# To sort dictionary values
import operator 
## Preprocessing
import pandas as pd
pd.set_option('display.max_colwidth', -1)
import os


# ### Connect to Twitter

# In[2]:


import tweepy
import config
    
# initialize api instance\n
consumer_key= config.consumer_key
consumer_secret= config.consumer_secret
access_token=config.access_token
access_token_secret =config.access_token_secret

#Connect to Twitter through the API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth,wait_on_rate_limit=True) 


# ### Get Twitter Trends

# In[3]:


def get_trends_by_location(loc_id,count):
    '''Get Trending Tweets by Location'''
    import iso639
    import numpy as np
    from langdetect import detect
    df = pd.DataFrame([])
    try:
        trends = api.trends_place(loc_id)
        df = pd.DataFrame([trending['name'],  trending['tweet_volume'], iso639.to_name(detect(trending['name']))] for trending in trends[0]['trends'])
        df.columns = ['Trends','Volume','Language']
        #df = df.sort_values('Volume', ascending = False)
        return(df[:count])
    except Exception as e:
        pass
        print("An exception occurred: ",e)
        df = pd.DataFrame([trending['name'],  trending['tweet_volume'], np.nan] for trending in trends[0]['trends'])
        df.columns = ['Trends','Volume','Language']
        return(df[:count])
    


# ### Get Translated Tweets

# In[5]:


def get_translation(text):
    ''' Translate Tweets in English'''
    from googletrans import Translator  # Import Translator module from googletrans package
    try:
        translator = Translator() # Create object of Translator.
        translated = translator.translate(text,dest='en')
        return(translated.text)
    except Exception as e:
        print("Exception", e)
        return 'NA'


# ### Get Tweets for a Hashtag

# In[7]:


def get_related_tweets(search_keyword):
    ''' collect tweets '''
    try: 
        count = 50
        # Create Blank Dataframe\n",
        df_tweets = pd.DataFrame(pd.np.empty((0, 1)))
        for keyword in search_keyword:
            # Remove Retweets
            search_tag = keyword +  "-filter:retweets" +  "-filter:media"
            
            print('Searching tweets for: ', search_tag)
    
            fetched_tweets = tweepy.Cursor(api.search,
                                q=search_tag,
                                lang="en").items(50)
            # Add records to the dataframe
            df_tweets = df_tweets.append([[tweet.text] for tweet in fetched_tweets])
            # Add columns
            df_tweets.columns = ['tweets']
            #clean emojis and pictures from tweets
            df_tweets['tweets'] = df_tweets['tweets'].str.replace(r'[^\x00-\x7F]+', '', regex=True)
            # Retuen Data
            return(df_tweets)
    except Exception as e:
        print('Encountered Exception:', e)
        return None


# ### Predict Emotion behind tweets

# In[8]:


def predict_emotion(tweets):
    '''Predict Emotions behind tweets'''
    from sklearn.pipeline import Pipeline
    # import joblib
    from joblib import load
    try:
        # load the saved pipleine model
        pipeline = load("text_classification.joblib")
        # get the prediction
        tweets['Prediction'] = pipeline.predict(tweets['tweets'])
        return tweets
    except Exception as e:
        print("Exception in predict_emotion: ", e)


# ### Clean the Tweets

# In[9]:


def data_cleaning(df_tweets):
    '''Clean the Tweets'''
    # convert to lower case
    df_tweets['clean_text'] = df_tweets['tweets'].str.lower()
    # Remove punctuations
    df_tweets['clean_text'] = df_tweets['clean_text'].str.replace('[^\w\s]',' ')
    # Remove spaces in between words
    df_tweets['clean_text'] = df_tweets['clean_text'].str.replace(' +', ' ')
    # Remove Numbers
    df_tweets['clean_text'] = df_tweets['clean_text'].str.replace('\d+', '')
    # Remove trailing spaces
    df_tweets['clean_text'] = df_tweets['clean_text'].str.strip()
    # Remove URLS
    df_tweets['clean_text'] = df_tweets['clean_text'].apply(lambda x: re.split('https:\/\/.*', str(x))[0])
    # remove stop words
    stop = stopwords.words('english')
    stop.extend(["amp","https","co","rt","new","let","also","still","one","people","gt"])
    df_tweets['clean_text'] =  df_tweets['clean_text'].apply(lambda x: " ".join(x for x in x.split() if x not in stop ))

    # Remove Text Column
    del df_tweets['tweets']
    # Rename the clean_text column as tweets
    df_tweets.rename(columns = {'clean_text':'Tweets'}, inplace = True) 
    return(df_tweets)


