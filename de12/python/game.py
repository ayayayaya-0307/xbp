import random
import time

def roledice():
    return random.randint(1,6)

def main():
    print("競馬場へようこそ！")
    time.sleep(1)
    print("ここは競馬場。さっそく予測を立ててみましょう！")
    time.sleep(1)
    print("一番人気、エクスビジネスー")
    time.sleep(1.7)
    print("二番人気、ジュギョネムイ")
    time.sleep(1.7)
    print("三番人気、オヤツマダカー")
    time.sleep(1.7)
    print("四番人気、アイワントタンイ")
    time.sleep(1.7)
    print("五番人気、カダイオワラン")
    time.sleep(1.7)
    gess=int(input("どの馬が優勝すると思い思いますか？(人気番号の数字で教えてください)"))

    print("レースが始まりました。")
    keika=random.randint(1,6)
    time.sleep(1)
    print("さあ、真っ先に飛び出したのは",str(keika),"番人気の馬です。")
    time.sleep(2)
    keikaa=random.randint(1,6)
    print("おおっと！ここで",str(keikaa),"番の馬が前に躍り出た！")
    time.sleep(2)
    print("さあ、最終的なレースの結果は……")
    time.sleep(3)
    kekka=random.randint(1,6)
    print("確定しました！",str(kekka),"番の優勝です！！")
    time.sleep(2)

    if gess == kekka:
        print("おめでとう御座います！")
    else:
        print("残念でした……")
main()

