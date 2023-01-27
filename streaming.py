from pytchat import LiveChat
import pafy
import pandas as pd
import time
# AIzaSyDKxTiE9QdseNW29_P4fSyPX0K1M7QxV-c

# api key, video id 입력
pafy.set_api_key('AIzaSyDKxTiE9QdseNW29_P4fSyPX0K1M7QxV-c')
video_id = 'FmfAvNsMVmw'

#  라이브 방송 정보 획득
v = pafy.new(video_id)
title = v.title
author = v.author
published = v.published

print(title)
print(author)
print(published)

# csv 생성
empty_frame = pd.DataFrame(columns=['제목', '채널 명', '스트리밍 시작 시간', '댓글 작성자', '댓글 내용', '댓글 작성 시간'])
empty_frame.to_csv('C:/Users/KimJihong/Desktop/김지홍/개발/댓글/youtube.csv')

chat = LiveChat(video_id = video_id, topchat_only = 'FALSE')

while chat.is_alive():
    time.sleep(5)
    try:
        data = chat.get()
        items = data.items
        for c in items:
            print(f"{c.datetime} [{c.author.name}]- {c.message}")
            data.tick()
            data2 = {'제목' : [title], '채널 명' : [author], '스트리밍 시작 시간' : [published], '댓글 작성자' : [c.author.name], '댓글 내용' : [c.datetime], '댓글 작성 시간' : [c.message]}
            result = pd.DataFrame(data2)
            result.to_csv('C:/Users/KimJihong/Desktop/김지홍/개발/댓글/streaming.csv', mode='a', header=False)
        time.sleep(3)
    except KeyboardInterrupt:
        chat.terminate()
        break