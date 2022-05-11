import urllib.request as req
import bs4
url = "https://www.ptt.cc/bbs/Stock/index.html"
request = req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
})
with req.urlopen(request)as respodse:
    deta = respodse.read().decode("utf-8")
print(deta)
root = bs4.BeautifulSoup(deta,"html.parser")
titles = root.find_all("title")
for i in titles:
    print(i)

