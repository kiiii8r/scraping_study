import requests
url = "https://creaters-you.com/"
response = requests.get(url)

# 取得したコードを整形する
response.encoding=response.apparent_encoding
print(response.text)