###練習學習寫入檔案
# f = open("have.txt",mode="w",encoding="UTF-8")#開啟
# f.write("5\n3")#寫入
# f.close()
# with open("have.txt",mode="w",encoding="UTF-8") as file:#最佳寫法(實務)
#     file.write("5\n3")#寫入
#     file.close()
# ###練習學習讀取檔案
# with open("have.txt",mode="r",encoding="UTF-8") as file:#開啟
#     sum = 0#sum設定寫0
#     for line in file:#一行一行加起來(讀取)
#         sum+=int(line)
# print(sum)#8
###怎麼使用json來學習讀取、複寫檔案
import json
with open("hello.json" ,"r",encoding="UTF-8") as jsonfile:#開啟
    data=json.load(jsonfile)#讀取方式
#print(d)列印{'name': 'tony', 'version': '3.5.4'}
data["name"]="new name"
with open("hello.json" ,"w",encoding="UTF-8") as jsonfile:#開啟
    json.dump(data,jsonfile)#複寫方式
