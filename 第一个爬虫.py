from urllib.request import urlopen

url="https://wap.baidu.com"

response=urlopen(url)

info=response.read()

print(info.decode())