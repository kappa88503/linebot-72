# app.py
import random
# import sqlite3
from datetime import datetime, timezone, timedelta

# import time
import pinyin
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from linebot.models import *
# -----------------------------------------------------------------------------------------------
app = Flask(__name__)
# -----------------------------------------------------------------------------------------------
line_bot_api = LineBotApi(
    'vpVg86tVKnbsIFw2JlicqbxPhzIeD246B5asVzbwMBCaalUGr5rdb1ghL5SeJeD+mJAWgqzH+QGDL76KA6Ns7uyPjK57WhartmXtxcZFxeOaB14PyEp6ITfKRguKnBSQswi+5kQixxzWvx0VLNdk4QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ed9c515dac10991c798d4e2a559fa667')
# -----------------------------------------------------------------------------------------------
# def

# -----------------------------------------------------------------------------------------------
wek_curriculum = [['跑班選修', '跑班選修', '跑班選修', '跑班選修', '午休', '選物四', '數學甲', '選化三', '放學啦'],
                  ['英語文', '國語文', '國語文', '數學甲', '午休', '英文作文', '藝生', '藝生', '化學課輔'],
                  ['數學甲', '彈性學習', '彈性學習', '彈性學習', '午休', '選物三-1', '體育', '國語文', '放學啦'],
                  ['數學甲', '國語文', '跑班選修', '跑班選修', '午休', '英語文', '選物四', '選化五-1', '放學啦'],
                  ['英文作文', '體育', '綜合活動', '綜合活動', '午休', '選化三', '跑班選修', '跑班選修', '放學啦']]

# -----------------------------------------------------------------------------------------------
toto_text = ['text']
# -----------------------------------------------------------------------------------------------
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
# -----------------------------------------------------------------------------------------------

tt = ''
# -----------------------------------------------------------------------------------------------

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global wek_curriculum, toto_text,tt
    msg = event.message.text
    # print(msg)
    msg = msg.encode('utf-8')
    line_text = event.message.text
    if event.message.text == tt:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))
        tt = ''
    else:
        tt = event.message.text
        

    if line_text == "骰子":
        r = random.randint(1, 6)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=f'擲出 {r} 點'))

    if line_text == "猜拳":
        mora_list = ['剪刀', '石頭', '布']
        mora = str(random.choice(mora_list))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=mora))

    if line_text == "不要問給我來一本正經的漫畫":
        sex_book = 'https://nhentai.net/g/' + str(random.randint(111111, 369999))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=sex_book))

    if '我出' in line_text:
        mora_list = ['剪刀', '石頭', '布']
        if '剪刀' in line_text:
            a = random.choice(mora_list)
            mora_player = '剪刀'
            if a == '石頭':
                mora_end = '我贏了'
            elif a == '布':
                mora_end = '你贏了'
            else:
                mora_end = '沒輸沒贏'
            mora_txt = f'你出:{mora_player}\n我出:{a}\n\n結果:{mora_end}'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=mora_txt))
        elif '石頭' in line_text:
            a = random.choice(mora_list)
            mora_player = '石頭'
            if a == '剪刀':
                mora_end = '你贏了'
            elif a == '布':
                mora_end = '我贏了'
            else:
                mora_end = '沒輸沒贏'
            mora_txt = f'你出:{mora_player}\n我出:{a}\n\n結果:{mora_end}'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=mora_txt))
        elif '布' in line_text:
            a = random.choice(mora_list)
            mora_player = '布'
            if a == '石頭':
                mora_end = '你贏了'
            elif a == '剪刀':
                mora_end = '我贏了'
            else:
                mora_end = '沒輸沒贏'
            mora_txt = f'你出:{mora_player}\n我出:{a}\n\n結果:{mora_end}'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=mora_txt))

    if '不要問選一個 ' in line_text:
        event.message.text = event.message.text.replace('不要問選一個 ', '')
        ran_ran = event.message.text.split('/')
        ran_ran = f'我選 {random.choice(ran_ran)}'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=ran_ran))

    if ('星期' in line_text or '禮拜' in line_text) and '課表' in line_text:

        txt = list(line_text)
        if len(txt) != 5:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='請輸入要查詢禮拜幾的課表'))
        elif txt[2] == '一':
            cur_text = '\n'.join(wek_curriculum[0])
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=cur_text))
        elif txt[2] == '二':
            cur_text = '\n'.join(wek_curriculum[1])
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=cur_text))
        elif txt[2] == '三':
            cur_text = '\n'.join(wek_curriculum[2])
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=cur_text))
        elif txt[2] == '四':
            cur_text = '\n'.join(wek_curriculum[3])
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=cur_text))
        elif txt[2] == '五':
            cur_text = '\n'.join(wek_curriculum[4])
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=cur_text))
        elif txt[2] == '六' or txt[2] == '日':
            cur_text = '放假啦'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=cur_text))
        else:
            cur_text = f'沒有星期{txt[2:-2]}'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=cur_text))
    if line_text == '下一節':
        utc_0 = datetime.utcnow().replace(tzinfo=timezone.utc)
        utc_8 = utc_0.astimezone(timezone(timedelta(hours=8)))  # 轉換時區到UTC+8
        wek = utc_8.weekday() + 1
        th = utc_8.hour
        tm = utc_8.minute
        if wek <= 5:
            if 6 <= th <= 17:
                if th == 6 or th == 7 or (th == 8 and tm <= 10):
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=wek_curriculum[wek - 1][0]))
                elif th == 8 and tm >= 10:
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=wek_curriculum[wek - 1][1]))
                elif th == 9:
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=wek_curriculum[wek - 1][2]))
                elif th == 10:
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=wek_curriculum[wek - 1][3]))
                elif th == 11:
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=wek_curriculum[wek - 1][4]))
                elif th == 12:
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=wek_curriculum[wek - 1][5]))
                elif th == 13 or (th == 14 and tm <= 10):
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=wek_curriculum[wek - 1][6]))
                elif th == 14:
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=wek_curriculum[wek - 1][7]))
                elif th == 15:
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=wek_curriculum[wek - 1][8]))
                else:
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(text='放學啦'))

            else:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='放學啦'))
        else:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='放假啦'))

    if '@拼音 ' in line_text:
        line_text = line_text.replace('@拼音 ', '')
        txt = pinyin.get(f'{line_text}', delimiter=' ', format='strip')
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=txt))

    if line_text.lower() == "test":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://imgur.com/7GR841j.png', preview_image_url='https://imgur.com/7GR841j.png'))
        #line_bot_api.reply_message(event.reply_token, TextSendMessage(text='伺服器連線正常'))
    
    if '@算術 ' in line_text:
        line_text = line_text.replace('@算術 ', '')
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=eval(line_text)))
        
    if '@隨機數' in line_text:
        line_text = line_text.replace('@隨機數 ', '')
        t1,t2 = map(int, input().split("，"))
        line_text = random.randint(t1,t2)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=line_text))
# -----------------------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run()
