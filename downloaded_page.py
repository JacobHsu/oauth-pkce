import requests

url = "https://www.oauth.com/playground/auth-dialog.html"  # 要下载的网页的URL

# 发送GET请求获取网页内容
response = requests.get(url)

if response.status_code == 200:
    # 将网页内容保存到文件
    with open("downloaded_page.html", "w", encoding="utf-8") as file:
        file.write(response.text)
        print("网页下载完成")
else:
    print("无法下载网页")
