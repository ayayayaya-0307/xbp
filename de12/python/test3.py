import requests as web
from bs4 import BeautifulSoup

#検索キーワード
keyword = '犬'

#リクエストヘッダー　
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

#ひとまず上位10件まで検索結果を取得
url = 'https://www.google.co.jp/search?hl=ja&num=10&q=' + keyword

#接続
response = web.get(url, headers=headers)

#HTTPステータスコードをチェック（200以外は例外処理）
response.raise_for_status()

#取得したHTMLをパース
soup = BeautifulSoup(response.content, 'html.parser')

#検索結果のタイトルとリンクを取得
ret_link = soup.select('.r > a')

title_list = []
url_list = []

for i in range(len(ret_link)):
# タイトルのテキスト部分を取得
 title_txt = ret_link[i].get_text()
 
# リンクのみを取得し、余計な部分を削除する
 url_link = ret_link[i].get('href').replace('/url?q=','')
 
 title_list.append(title_txt)
 url_list.append(url_link)
 
#検索結果を表示
for i in range(len(title_list)):
 print(title_list[i])
 print(url_list[i])
 print('')