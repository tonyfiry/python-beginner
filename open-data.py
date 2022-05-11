# #網路資料
# # import urllib.request as request
# # url = "https://www.ntu.edu.tw/"
# # with request.urlopen(url) as response:
# #     deta = response.read().decode("utf-8")
# # print(deta)

# #讀取json格式，擷取公開資料
# import urllib.request as request
# import json
# url = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
# with request.urlopen(url) as response:
#     deta = json.load(response)
# #print(deta)
# #取得公司名稱
# clist = deta["result"]["results"]
# with open("deta.txt","w",encoding="UTF-8") as file:
#     for conpany in clist:
#         file.write(conpany["公司名稱"]+"\n")


import urllib.request as request
import json
url = "https://data.taipei/api/v1/dataset/5be33495-7594-4f32-ab63-474640059bb2?scope=resourceAquire"
with request.urlopen(url) as response:
    deta = json.load(response)
#print(deta)

clist=deta['result']['results']
with open('deta2.txt',"w",encoding="utf-8") as file:
    for conpany in clist:
        file.write(conpany["內湖科技園區營業收入[億元]"]+"\n")


