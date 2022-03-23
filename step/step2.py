from curses import A_ALTCHARSET
import requests
url = "https://creaters-you.com/"
response = requests.get(url)

response.encoding=response.apparent_encoding
filename = "download.txt"

# open ファイルを開く
# パーミッション(w:書き込みモード a:追記 r:読み込み専用 at:書き足し)
f = open(filename, mode="w")  

# write ファイルに書き込む
f.write(response.text)

# ファイルを閉じる
f.close()

# 省略形(開いて書き込んで閉じる)
with open(filename, mode="w") as f:
  f.write(response.text)