###利用上課的的實際寫過一遍
# class point:#先定義類別
#     def __init__(self):#先定義類別屬性
#         self.x=3#實體物件1
#         self.y=4#實體物件2
# d1=point()#實體屬性1
# print(d1.x+d1.y)#印出7


# class point:
#     def __init__(self):
#         self.name = "小明"
#         self.data = "2019-03-10"
# d1 = point()
# print(d1.name+"\n"+d1.data)

class kig:
    def __init__(self,name):
        self.name = name
        self.file = None#假設裡面是空的
    def open(self):
        self.file=open(self.name,"w",encoding="utf-8")
    def write(self):
        return self.file.write("你寫")
d1 = kig("d1.txt")
d1.open()
w=d1.write()
print(w) 