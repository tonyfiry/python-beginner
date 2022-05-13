#載入 pandas 模組
import pandas as pd
#建立Series
# data = pd.Series([1,2,3])
# #基本Series 操作
# # print(data)
# print("MAX",data.max())#最大值
# print("MIN",data.min())#最小值
# print("median",data.median())#中位數
# print("mean",data.mean())#平均值
# data = data*2#乘兩倍
# print(data)
#DataFrame
data = pd.DataFrame({
    "name":["ady","feg","mrea"],
    "price":[100,230,800]
})
#基本DataFrame 操作
print(data)#雙維度資料(Table)
print("==============")
print(data["name"])#取得直向資料
print("==============")
print(data.iloc[0])#取得橫向資料