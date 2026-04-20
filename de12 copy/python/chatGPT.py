import openai

# APIキーをセット
openai.api_key = "sk-\(・＿・)/"
question = "以下の単語を使って"

# ChatGPTにテキスト生成をリクエスト
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": question}
    ]
)

# 生成されたテキストを表示
print(response["choices"][0]["message"]["content"])