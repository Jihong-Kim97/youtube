from numpy import empty_like
import pandas
import pafy
from googleapiclient.discovery import build
 
 
api_key = 'AIzaSyDKxTiE9QdseNW29_P4fSyPX0K1M7QxV-c'
video_id = '2KxEIeVNOtQ'
 
comments = list()
shorts = list()
pafy.set_api_key('AIzaSyDKxTiE9QdseNW29_P4fSyPX0K1M7QxV-c')
v = pafy.new(video_id)
title = v.title
author = v.author
published = v.published

api_obj = build('youtube', 'v3', developerKey=api_key)
response = api_obj.commentThreads().list(part='snippet,replies', videoId=video_id, maxResults=100).execute()
 
while response:
    for item in response['items']:
        time = ""
        comment = item['snippet']['topLevelComment']['snippet']
        comments.append([comment['textDisplay'], comment['authorDisplayName'], comment['publishedAt'], comment['likeCount']])
        if video_id in comment['textDisplay']:
            comment_short_list = comment['textDisplay'].replace('<','|').replace('>','|').split('|')
            empty_content = True
            for comment_short in comment_short_list:
                if ":" in comment_short and not "a" in comment_short:
                    time = str(comment_short)
                elif not "a" in comment_short and not "br" in comment_short and not time == "":
                    content = comment_short
                    empty_content = False
                    shorts.append([comment['authorDisplayName'], time, content, comment['likeCount']])
                    time = ""

            if empty_content:
                shorts.append([time, content, comment['textDisplay'], comment['authorDisplayName'], comment['publishedAt'], comment['likeCount']])
 
        if item['snippet']['totalReplyCount'] > 0:
            for reply_item in item['replies']['comments']:
                reply = reply_item['snippet']
                comments.append([reply['textDisplay'], reply['authorDisplayName'], reply['publishedAt'], reply['likeCount']])
 
    if 'nextPageToken' in response:
        response = api_obj.commentThreads().list(part='snippet,replies', videoId=video_id, pageToken=response['nextPageToken'], maxResults=100).execute()
    else:
        break
 
df_comments = pandas.DataFrame(comments)
df_comments.to_csv('C:/Users/KimJihong/Desktop/김지홍/개발/댓글/{}.csv'.format(title), header=['comment', 'author', 'date', 'num_likes'], index=None)

df_shorts = pandas.DataFrame(shorts)
df_shorts.to_csv('C:/Users/KimJihong/Desktop/김지홍/개발/댓글/{}_shorts.csv'.format(title), header=['author','time', 'content', 'num_likes'], index=None)