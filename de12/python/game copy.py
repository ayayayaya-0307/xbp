import random
import time
import numpy as np

def main():
    print("競馬場へようこそ！")
    time.sleep(1)
    print("ここは競馬場。さっそく予測を立ててみましょう！")
    time.sleep(1)
    print("一番人気、エクスビジネスー")
    time.sleep(0.7)
    print("二番人気、ジュギョネムイ")
    time.sleep(0.7)
    print("三番人気、オヤツマダカー")
    time.sleep(0.7)
    print("四番人気、アイワントタンイ")
    time.sleep(0.7)
    print("五番人気、カダイオワラン")
    time.sleep(0.7)
    gess=int(input("どの馬が優勝すると思い思いますか？(人気番号の半角数字で教えてください)"))

    print("レースが始まりました。")
    time.sleep(1)

    keika=random.randint(1,6)
    print("さあ、真っ先に飛び出したのは",str(keika),"番人気の馬です。")
    time.sleep(2)

    keikaa=random.randint(1,6)
    while keikaa == keika:
        keikaa=random.randint(1,6)
    print("おおっと！ここで",str(keikaa),"番の馬が前に躍り出た！")
    time.sleep(2)

    saigo=random.randint(1,6)
    saigoo=random.randint(1,6)
    while saigoo == saigo:
        saigoo=random.randint(1,6)
    print("最終コーナー、先頭で競り合っているのは",str(saigo),"番、",str(saigoo),"番の二頭です！")
    time.sleep(2)

    print("さあ、最終的なレースの結果は……")
    time.sleep(3)
    uma=[1,2,3,4,5]
    weights=[0.3,0.3,0.2,0.1,0.1]
    kekka=np.random.choice(uma,p=weights)
    print("確定しました！",str(kekka),"番人気の馬の優勝です！！")
    time.sleep(2)

    print("あなたが予想したのは",gess,"番人気の馬です。")
    time.sleep(2)
    if gess == kekka:
        print("おめでとう御座います！")
    else:
        print("残念でした……")
main()
