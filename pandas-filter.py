import pandas as pd
#篩選資料練習-Series
data = pd.Series(["price","pople","tony"])
print(data.loc[0])#Series
# condition = data.str.contains("p")
# print(condition)
# filteredData = data[condition]
# print(filteredData)

#篩選資料練習-DataFrame

# data = pd.DataFrame({
#     "name":["Amy","Bob","Charles"],
#     "salary":[30000,50000,40000]
# },index=[1,2,3])
# condition = data["salary"]>=40000
# print(condition)
# filteredData = data[condition]
# print(filteredData)
#print(data.iloc[1])#DataFrame


