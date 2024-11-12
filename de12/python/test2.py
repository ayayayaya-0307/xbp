import wikipedia
import time

# キーワードを設定
kansu=input("検索したいことを入力してね")

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

print("-------スペイン語---------")
wikipedia.set_lang("sp")
result = wikipedia.search(keyword)
print("検索結果",result)
time.sleep(2)

print("-------ポルトガル語---------")
wikipedia.set_lang("pt")
result = wikipedia.search(keyword)
print("検索結果",result)
time.sleep(2)
#print("最初の検索結果を表示")
#page_data = wikipedia.page(result[0])
#print(page_data.content)

