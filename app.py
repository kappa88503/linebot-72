# app.py
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
import random
from datetime import datetime
# -----------------------------------------------------------------------------------------------
app = Flask(__name__)
# -----------------------------------------------------------------------------------------------
line_bot_api = LineBotApi('vpVg86tVKnbsIFw2JlicqbxPhzIeD246B5asVzbwMBCaalUGr5rdb1ghL5SeJeD+mJAWgqzH+QGDL76KA6Ns7uyPjK57WhartmXtxcZFxeOaB14PyEp6ITfKRguKnBSQswi+5kQixxzWvx0VLNdk4QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ed9c515dac10991c798d4e2a559fa667')
# -----------------------------------------------------------------------------------------------
# def

# -----------------------------------------------------------------------------------------------
wek_curriculum = [['跑班選修', '跑班選修', '跑班選修', '跑班選修', '選物四', '數學甲', '選化三'],
                  ['英語文', '國語文', '國語文', '數學甲', '英文作文', '藝生', '藝生', '化學課輔'],
                  ['數學甲', '彈性學習', '彈性學習', '彈性學習', '選物三-1', '體育', '國語文'],
                  ['數學甲', '國語文', '跑班選修', '跑班選修', '英語文', '選物四', '選化五-1'],
                  ['英文作文', '體育', '綜合活動', '綜合活動', '選化三', '跑班選修', '跑班選修']]
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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    #print(msg)
    msg = msg.encode('utf-8')
    line_text = event.message.text
        
    if line_text == "骰子":
        r = random.randint(1,6)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=f'擲出 {r} 點'))
        
    if line_text == "猜拳":
        mora_list = ['剪刀', '石頭', '布']
        mora = str(random.choice(mora_list))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=mora))        

    if line_text == "不要問給我來一本正經的漫畫":
        sex_book = 'https://nhentai.net/g/' + str(random.randint(111111, 369999))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=sex_book))
        
    if line_text == "我出剪刀":
        mora_list = ['剪刀', '石頭', '布']
        mora_player = '剪刀'
        a = random.choice(mora_list)
        if a == '石頭':
            mora_end = '我贏了'
        elif a == '布':
            mora_end = '你贏了'
        else:
            mora_end = '沒輸沒贏'
        mora_txt = f'你出:{mora_player}\n我出:{a}\n\n結果:{mora_end}'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=mora_txt))

    elif line_text == "我出石頭":
        mora_list = ['剪刀', '石頭', '布']
        mora_player = '石頭'
        a = random.choice(mora_list)
        if a == '剪刀':
            mora_end = '你贏了'
        elif a == '布':
            mora_end = '我贏了'
        else:
            mora_end = '沒輸沒贏'
        mora_txt = f'你出:{mora_player}\n我出:{a}\n\n結果:{mora_end}'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=mora_txt))

    elif line_text == "我出布":
        mora_list = ['剪刀', '石頭', '布']
        mora_player = '布'
        a = random.choice(mora_list)
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
        
    if line_text == "test" or line_text == "Test":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='伺服器連線正常'))

    if ('星期' in line_text or '禮拜' in line_text) and '課表' in line_text:
        txt = list(line_text)
        if txt[2] == '一':
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='\n'.join(wek_curriculum[0]))

        elif txt[2] == '二':
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='\n'.join(wek_curriculum[1]))

        elif txt[2] == '三':
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='\n'.join(wek_curriculum[2]))

        elif txt[2] == '四':
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='\n'.join(wek_curriculum[3]))

        elif txt[2] == '五':
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='\n'.join(wek_curriculum[4]))

        elif txt[2] == '六' or txt[2] == '日':
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='放假啦')

        else:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=f'沒有星期{txt[2:-2]}')



 # -----------------------------------------------------------------------------------------------       
if __name__ == "__main__":
    app.run()
