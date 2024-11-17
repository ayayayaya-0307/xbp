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
#↑指定したファイルを開き、書き込みモード（ｗ）にし、UTF-8でファイルを扱うと指定する


#_2DunygeBZHdgHX_Gih3GC4というクラスのリンクとテキストを持ってくる指示。
    topic = soup.find(class_="_2DunygeBZHdgHX_Gih3GC4")
    #先ほど解析したHTMLコンテンツから「_2DunygeBZHdgHX_Gih3GC4」という項目を探し、topicに定義する
    for element in topic.find_all("a"):
    #topicの中から「a」というタグのテキストをすべて探し、順番に処理する
        print(element.text)
        #現在処理しているタグの文言を表示する。
        #例: <a href="example.com">Example</a> の場合、"Example"が表示される。
        url2 = element.get("href")
        #テキストのhref属性（URLみたいなの）を取得する。
        link_url = urllib.parse.urljoin(url,url2)
        #URLみたいなのを完全なURLにする
        #例: url = "https://www.yahoo.co.jp/l" と url2 = "/page" なら、link_urlは"https://www.yahoo.co.jp/l/page"になる。
        f.write(element.text+"\n")
        f.write(link_url+"\n")
        f.write("\n")
        #それぞれファイルに書き起こす

print(" ")
time.sleep(1)
print("本日のニュースは以上です")
time.sleep(1)
print("何か気になる用語はありますか？")
time.sleep(1)
print("WikipediaとGoogleで検索できます")
time.sleep(1)
print("　")
kansu=input("検索：")
print("-------------------")


def google_search(query, num_results=10):
    # 検索クエリをURLに変換する
    query = query.replace(' ', '+')
    url = f"https://www.google.com/search?q={query}&num={num_results}"
    
    #ブラウザのふりをする
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    
    # Google検索ページを取得する
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 検索結果を抽出する
    results = []
    for g in soup.find_all('div', class_='tF2Cxc'):
        title = g.find('h3')
        link = g.find('a')['href']
        snippet = g.find('span', class_='aCOpRe')
        if title and link:
            results.append({
                "title": title.text,
                "link": link,
                "snippet": snippet.text if snippet else "説明なし"
            })
    
    return results

# 実行
print("　")
print("Google")
print(" ")
search_results = google_search(kansu, num_results=5)
for result in search_results:
    print(f"タイトル: {result['title']}")
    print(f"リンク: {result['link']}")
    print(f"スニペット: {result['snippet']}")
    time.sleep(2)
    print("-" * 50)

print(" ")
time.sleep(1)
print("続いて、Wikipediaでも検索しますか？")
time.sleep(1)
yesorno = input("検索を続ける場合は「YES」と、プログラムを終了する場合は「NO」と書いてください。")
time.sleep(1)
if yesorno == ("YES"):
    print(" ")
    print("Wikipedia")
    print(" ")
    wikipedia.set_lang("ja")
    result = wikipedia.search(kansu)
    print("検索結果",result)
    time.sleep(3)
    print(" ")

    print("最初の検索結果を表示")
    page_data = wikipedia.page(result[0])
    print(page_data.content)
    time.sleep(1)


print(" ")
print("これで終わります")

