name=input("名前を入力してください")
kokugo=int(input("国語の点数は？"))
sansu=int(input("算数の点数は？"))

print(name, "さんは国語が", kokugo, "点で算数は",sansu, "点ですね。")

if kokugo>=90 and sansu>=90:
    ono=input("本当ですか？（yesかnoで答えてください）")
    if ono==("yes"):
        print(name,"さん、あなたは賢いです")
    elif ono==("no"):
        print("素直でよろしい")
    else:
        print("yesかnoで答えろって言ったのに…")
elif kokugo>=75 and sansu<50:
    print(name,"さん、あなたは文系です")
elif kokugo<50 and sansu>=75:
    print(name,"さん、あなたは理系です")
elif kokugo<20 and sansu<20:
    print(name,"さん、あなたは馬鹿です")
else:
    print(name,"さん、あなたは普通です")

