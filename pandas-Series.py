import pandas as pd
#資料索引
# data = pd.Series([22,30,41,53],index=["a","b","c","d"])#index="a"= 0,"b"= 1,"c"=2,"d"=3
#觀察資料
#print(data)#顯示資料
# print(data.index)
# print(data.size)

#取得資料:
# print(data[0],data[3])
# print(data["a"],data["d"])

#數字運算:
# print(data.max())
# print(data.min())
# print(data.median())
# print(data.std())
#字串運算:
data = pd.Series(["hello","tony","tice","zice"],index=["a","b","c","d"])
print("================")
print(data.str.len())#len是一個單字裡面幾個字
print("================")
print(data.str.lower())
print("================")
print(data.str.upper())
print("================")
print(data.str.cat(sep=","))
print("================")
print(data.str.replace("hello","dony"))#replace是替代
print("================")
print(data.str.contains("o"))#