import requests
from bs4 import BeautifulSoup
import urllib
import wikipedia
import time


url = "https://www.yahoo.co.jp/l"
#↑取得したいWEBページのURL
html = requests.get(url)
#↑指定したURLにGETリクエストを送り、HTMLコンテンツを取得
soup = BeautifulSoup(html.content,"html.parser")
#取得したHTMLコンテンツを解析し、操作可能なオブジェクトに変換

filename = "linklist.text"
#↑書き込みたいファイルを指定
with open(filename,"w", encoding="utf-8") as f:
#指定したファイルを開き、書き込みモード（ｗ）にし、UTF-8でファイルを扱うと指定する

#中身。_2DunygeBZHdgHX_Gih3GC4ていうクラスのリンクとテキストを持ってくる指示。
    topic = soup.find(class_="_2DunygeBZHdgHX_Gih3GC4")
    for element in topic.find_all("a"):
        print(element.text)
        url2 = element.get("href")
        link_url = urllib.parse.urljoin(url,url2)
        f.write(element.text+"\n")
        f.write(link_url+"\n")
        f.write("\n")

print(" ")
print("本日のニュースは以上です")
time.sleep(1)
print("何か気になる用語はありますか？")
print("関連用語を日本語と英語で検索します")
print("　")
kansu=input("ここに記入してください→")

keyword = kansu
# キーワードで検索
print("-------日本語---------")
wikipedia.set_lang("ja")
result = wikipedia.search(keyword)
print("検索結果",result)
print("　")
time.sleep(2)

print("-------英語---------")
wikipedia.set_lang("en")
result = wikipedia.search(keyword)
print("検索結果",result)
time.sleep(2)