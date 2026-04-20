import requests
from bs4 import BeautifulSoup

def google_search(query, num_results=10):
    # 検索クエリをURLエンコード
    query = query.replace(' ', '+')
    url = f"https://www.google.com/search?q={query}&num={num_results}"
    
    # ヘッダーを設定（ブラウザのふりをする）
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    
    # Google検索ページを取得
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("エラー: Googleへのアクセスが拒否されました")
        return []
    
    # HTMLをパース
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 検索結果を抽出
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

# 実行例
kensaku = input("検索したい用語を入力してください")
search_results = google_search(kensaku, num_results=5)
for result in search_results:
    print(f"タイトル: {result['title']}")
    print(f"リンク: {result['link']}")
    print(f"スニペット: {result['snippet']}")
    print("-" * 50)