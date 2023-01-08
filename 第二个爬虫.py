from urllib.request import urlopen
from urllib.request import Request
url="http://www.baidu.com"

request=Request(url)
response=urlopen(request)

info=response.read()

printf(info.decode())