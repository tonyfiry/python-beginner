import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"
request = req.Request(url,headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
})
with req.urlopen(request) as respondse:
    deta = respondse.read().decode("utf-8")
#print(deta)
#解析原始碼，來抓取更多標題
import bs4#匯入BeautifulSoup4模組
root = bs4.BeautifulSoup(deta,"html.parser")#lxml 套件是用來作為 BeautifulSoup 的解析器（Parser）。
titls = root.find_all("div",class_ = "title")#是<div class="title"></div>
with open("MV.txt","w",encoding="UTF-8") as file:#用檔案方式來寫入，並放在"MV.txt"
     for title in titls:
        if title.a != None:
            file.write(title.a.string+"\n")
