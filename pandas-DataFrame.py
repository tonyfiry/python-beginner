import pandas as pd
#寫入資料
data = pd.DataFrame({
    "name":["tony","dira","strga"],
    "program":["Python","Java","C++"]
},index=[1,2,3])

#新增資料
data["money"]=pd.Series([100,200,300],index=[1,2,3])
print(data)
#取得資料
print(data.loc[0],index=[1],sep="\n")
print(data.iloc[0],index=[1],sep="\n")
# print(data)#列印資料
print("=====================")

#觀察資料
# print(data.size)#列印資料數量
# print(data.index)#列印資料索引位置

#字串資料運算
# print(data["name"].str.upper())
# print(data["name"].str.cat(sep="\n"))



#數字資料運算
print("數字標準差:",data["money"].std())
print("數字平均值:",data["money"].mean())
print("數字加總:",data["money"].sum())



