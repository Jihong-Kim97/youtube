import pytchat 
import time
import pandas as pd

chat = pytchat.create(video_id="9Mk1oxBSnKI")
while chat.is_alive():
    #print(chat.get().json())
    #time.sleep(5)
    data = chat.get()
    items = data.items
    
    # Each chat item can also be output in JSON format.
    for c in chat.get().items:
        print(f"{c.datetime} [{c.author.name}]- {c.message}")
        data.tick()
        data2 = {'댓글 작성자' : [c.author.name], '댓글 내용' : [c.datetime], '댓글 작성 시간' : [c.message]}
        result = pd.DataFrame(data2)
        result.to_csv('C:/Users/KimJihong/Desktop/김지홍/개발/댓글/youtube.csv', mode='a', header=False, index=False)

    