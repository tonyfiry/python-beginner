# class point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def math(self):
#         print(self.x,self.y)
#     def result(self,one,two):
#         return (self.x+one)+(self.y+two)
# d = point(3,2)
# d.math()
# a = d.result(2,3)
# print(a)

##使用File來讀取(實體屬性，實體物件，實體方法)
class File:
    def __init__(self,name):
        self.name=name
        self.flie=None#初始設None，就是裡面空的
    def open(self):
        self.flie = open(self.name,"r",encoding="UTF-8")#檔案讀取方式
    def read(self):
        return self.flie.read()#完成讀取
d = File("d1.text")#d1.text檔案
d.open()
read1 = d.read()
print(read1)