import urllib.request as req
def Getdata(url):
    request = req.Request(url,headers={
        "cookie":"over18=1",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    })
    with req.urlopen(request) as respondse:
        deta = respondse.read().decode("utf-8")
    #print(deta)
    #解析原始碼，來抓取更多標題
    import bs4#匯入BeautifulSoup4模組
    root = bs4.BeautifulSoup(deta,"html.parser")#lxml 套件是用來作為 BeautifulSoup 的解析器（Parser）。
    titls = root.find_all("div",class_ = "title")#是<div class="title"></div>
    for title in titls:
        if title.a != None:
            print(title.a.string)
    #抓取上一頁的連結
    nextlink = root.find("a",string="‹ 上頁")
    return nextlink["href"]#列印是(/bbs/Gossiping/index39224.html)
PageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0#假設計數是零
while count <3:#列印3次(共3頁)
    PageURL = "https://www.ptt.cc" + Getdata(PageURL)
    count += 1



