import logging

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseBadRequest
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

from .models import Account,LineAccount

logger = logging.getLogger("django")

line_bot_api = LineBotApi(settings.CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(settings.CHANNEL_SECRET)

@csrf_exempt
@require_POST
def webhook(request: HttpRequest):
    signature = request.headers["X-Line-Signature"]
    body = request.body.decode()

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        messages = (
            "Invalid signature. Please check your channel access token/channel secret."
        )
        logger.error(messages)
        return HttpResponseBadRequest(messages)
    return HttpResponse("OK")

@handler.add(event=MessageEvent, message=StickerMessage)
def handl_stick_message(event: MessageEvent):
    reply_txt = TextSendMessage(text='看不懂你在說啥ＱＱ，請說中文')
    line_bot_api.reply_message(reply_token=event.reply_token, messages=reply_txt)

@handler.add(event=MessageEvent, message=TextMessage)
def handl_message(event: MessageEvent):
    Usertxt=event.message.text   #取得使用者輸入的文字
    print(Usertxt)
    # reply_txt = TextSendMessage(text=txt)
    # reply_stk = StickerSendMessage(package_id=1,sticker_id=13)
    # #貼圖包編號3、貼圖編號233(貼圖列表查詢網址:devdocs.line.me/files/sticker_list.pdf)

    # line_bot_api.reply_message(event.reply_token, [reply_txt, reply_stk])  #回復文字與指定貼圖
    LineIdDict = {i[0]:i[1] for i in LineAccount.objects.values_list('account','LineID')}
    userProfile = line_bot_api.get_profile(event.source.user_id)

    if userProfile.user_id not in LineIdDict.values():   ###確認使用者是否有帳號了
        if 'name:' in Usertxt and 'account:' in Usertxt and ';' in Usertxt:   
            UserDict = {i.split(':')[0]:i.split(':')[1] for i in Usertxt.split(';')}
            newUserCreat(event, UserDict, userProfile)  #確認差勤是否有此帳號，並建立帳號進資料庫
        else:   #無帳號，請使用者建立帳號
            newUserMessage(event,userProfile)
    else:
        cheakOldUserLine(userProfile)  #確認使用者Line資料是否變更<尚未啟用>

        # print(event.source.user_id,'2345') 

        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                # thumbnail_image_url='https://profile.line-scdn.net/0m02da21d272511f3175f4298d7ba30a44ab305821c0aa',
                title='景丰小幫手',
                text='以下為功能選單請依自身需求選取',
                actions=[
                    # MessageTemplateAction(
                    #     label='ButtonsTemplate',
                    #     text='ButtonsTemplate'
                    # ),
                    URITemplateAction(
                        label='線上打卡',
                        uri='https://liff.line.me/1654039770-MKpQzAy4'
                    ),
                    # PostbackTemplateAction(
                    # label='postback',
                    # text='postback text',
                    # data='postback1'
                    # )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)

def newUserMessage(event, profile):
    reply_txt = []
    reply_txt.append(TextSendMessage(text='嗨, '+profile.display_name+'您好:\n這是景丰Line機器人\n您是新使用者，麻煩幫我輸入您的全名及差勤系統帳號！\n請複製以下格式修改：'))
    reply_txt.append(TextSendMessage(text='name:王大明;account:jim'))
    # line_bot_api.reply_message(event.reply_token, 'reply_txt')  #回復文字
    line_bot_api.reply_message(reply_token=event.reply_token, messages=reply_txt)

def newUserCreat(event,UserDict,userProfile):
    AccountDict = {i[0]:i[1] for i in Account.objects.values_list('account', 'name')}
    LineExistAccount = [ i[0] for i in LineAccount.objects.values_list('account')]
    try:
        if UserDict['name'] == AccountDict[UserDict['account']]:
            if UserDict['account'] in LineExistAccount:    #確認帳號是否已經被註冊，沒有才能註冊帳號
                reply_txt = TextSendMessage(text=UserDict['account']+'已被其他使用者註冊，請聯繫管理員確認')
                line_bot_api.reply_message(reply_token=event.reply_token, messages=reply_txt)
            else:
                data = LineAccount()

                data.LineID = userProfile.user_id
                data.LineName = userProfile.display_name
                data.LinePic = userProfile.picture_url
                data.account = UserDict['account']
                data.name = UserDict['name']
                data.save()
                reply_txt = [TextSendMessage(text='帳號建立成功!')]
                print('帳號建立成功!')
                reply_txt.append(TextSendMessage(text='請輸入任何文字，我會丟選單給您'))
                line_bot_api.reply_message(reply_token=event.reply_token, messages=reply_txt)
        else:
            reply_txt = TextSendMessage(text='帳號與姓名無法對應，請重新輸入')
            line_bot_api.reply_message(reply_token=event.reply_token, messages=reply_txt)
    except KeyError:
        reply_txt = TextSendMessage(text='差勤系統上無此帳號，請重新輸入')
        line_bot_api.reply_message(reply_token=event.reply_token, messages=reply_txt)

def cheakOldUserLine(userProfile):  #確認使用者Line資料是否變更
    DB_userProfile = LineAccount.objects.get(LineID = userProfile.user_id)
    pass
    # newDB = LineAccount()

    # if DB_userProfile.LineName != userProfile.display_name:
    #     DB_userProfile.LineName = userProfile.display_name
    #     DB_userProfile.save()
    # if DB_userProfile.LinePic != userProfile.picture_url:
    #     DB_userProfile.LinePic = userProfile.picture_url
