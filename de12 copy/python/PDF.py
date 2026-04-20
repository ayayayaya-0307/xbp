import fitz  # PyMuPDF
from collections import Counter
import re

# PDFファイルを読み込んでテキストを抽出
def extract_text_from_pdf(pdf_path):
    text = "kannsatu.pdf"
    with fitz.open(pdf_path) as pdf_document:
        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]
            text += page.get_text()
    return text

# テキストから単語の頻度をカウント
def get_word_frequencies(text):
    # 単語を抽出（アルファベットや数字のみを対象）
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    return word_counts

# 使用例
pdf_path = 'kannsatu.pdf'  # 調べたいPDFのパス
text = extract_text_from_pdf(pdf_path)
word_frequencies = get_word_frequencies(text)

# 頻出単語トップ10を表示
for word, freq in word_frequencies.most_common(10):
    print(f'{word}: {freq}')