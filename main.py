#必要なライブラリを読み込む
from PIL import Image, ImageDraw, ImageFont, ImageFilter #画像処理に必要
import textwrap　#文字を折り返すのに必要
import requests　#APIリクエストに必要
import json　#jsonを扱うのに必要
import datetime #時間をとってくるのに必要
import tweepy　#twitterを投稿するの必要

#tweepyの設定（とりあえず何も考えずにつくっとけ）
consumer_key = "TwitterのAPI key"
consumer_secret = "TwitterのAPI key secret"
token = "TwitterのAccess token"
token_secret = "TwitterのAccess token secret"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token, token_secret)
api = tweepy.API(auth)

#変数各種設定
nomal_today = datetime.date.today() #2021-01-01
today = str(nomal_today) + 'T00:00:00.000Z' #2021-01-01T00:00:00.000Z
normal_today= str(nomal_today) #'2021-01-01'
now = datetime.datetime.today() #2021-01-01 21:04:15.412854
year = now.year # 2021
month = now.month # 1
day = now.day #1
hash_month = '{:02d}'.format(now.month) #01
hash_day = '{:02d}'.format(now.day) #01

# APIで令和市ホームページから情報をとってくる
API_Endpoint = "ホームページのAPIエンドポイント"
API_Key = "ホームページのAPIキー"
headers = {'Content-Type': 'application/json', 'Authorization':API_Key}
result = requests.get(API_Endpoint, headers=headers).json()
jsn = result['records']

# とってきた情報(JSON)から必要な値を取り出す関数
# [{key:tokyo, value:apple}{key:chiba, value:banana}]こういう形のJSONだった。親キーがないパターン。
def getValue(today, value, items):
values = [x[value] for x in items if 'New Property' in x and value in x and x['New Property'] == today]
return values[0] if values else ""

#画像作成に必要な各種設定
ogp_base_img_path = './bg.jpg' #背景の画像を指定
icon = getValue(today, 'emoji', jsn)　#アイコンの絵文字
title = getValue(today, 'Name', jsn)　#記念日の名前
text_discription = getValue(today, 'discription', jsn) #記念日の説明
creator = getValue(today, 'creator', jsn) #作った人

text_title = str(year) + '年' + str(month) + '月' + str(day) + '日は' +title　#タイトルの行を作成
text_created = "created by " + creator #作った人の行を作成
wrap_list = textwrap.wrap(text_discription, 48) # テキストを16文字で改行しリストwrap_listに代入

#フォントを指定
font_emoji_path = "NotoColorEmoji.ttf"
font_bold_path = "NotoSansJP-Bold.otf"
font_medium_path = "NotoSansJP-Medium.otf"

# 文字を書く関数
def add_centered_text(base_img, text, font_path, font_size, font_color, height):
 font = ImageFont.truetype(font_path, font_size)
 draw = ImageDraw.Draw(base_img)

 # 文字がベース画像からはみ出ないように処理
 if draw.textsize(text, font=font)[0] > base_img.size[0] - 170:
 while draw.textsize(text + '…', font=font)[0] > base_img.size[0] - 170:
 text = text[:-1]
 text = text + '…'
 draw.text(((base_img.size[0] - draw.textsize(text, font=font)[0]) / 2, height), text, font_color, font=font,)
 return base_img

# アイコンを書く関数
def add_icon(font, base_img, icon):
 fnt = ImageFont.truetype(font, size=109, layout_engine=ImageFont.LAYOUT_RAQM)
 draw = ImageDraw.Draw(base_img)
 draw.text((530, 120), icon, fill="#faa", embedded_color=True, font=fnt)

 return base_img

#文字を書く関数（折り返して説明文を表示する）関数
def add_line_text(base_img, text, font_path, font_size, font_color, height):
 font = ImageFont.truetype(font_path, font_size)
 draw = ImageDraw.Draw(base_img)
 line_counter = 0 # 行数のカウンター
 for line in wrap_list: # wrap_listから1行づつ取り出しlineに代入
 y = line_counter*48+400 # y座標をline_counterに応じて下げる
 draw.multiline_text((70, y),line, font_color, font=font) # 1行分の文字列を画像に描画
 line_counter = line_counter +1 # 行数のカウンターに1
 return base_img

message1 = '令和市では' + text_title + 'です。\n\n'
message2 = '#ThrowbackReiwaCity' + str(hash_month) +str(hash_day)
message = message1 + message2 #tweet用の文章を作成

#開いたら行うこと
if __name__ == '__main__':
 base_img = Image.open(ogp_base_img_path).copy()
 base_img = add_icon(font_emoji_path, base_img, icon)
 base_img = add_centered_text(base_img, text_title, font_bold_path, 48, (48, 48, 48), 280)
 base_img = add_line_text(base_img, text_discription, font_medium_path, 22, (120, 120, 120), 400)
 base_img = add_centered_text(base_img, text_created, font_medium_path, 22, (120, 120, 120), 580)
 base_img.show()
 base_img.save(f'{normal_today}.png')

 file = normal_today + '.png' #tweetしたいファイル名を指定
 api.update_with_media(filename=file, status=message)　#tweet
