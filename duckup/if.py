from email import message


message1 = int(input("你要付多少錢?"))


if message1 >=300:#假設你投入金額大於200
    print("我就請你吃義大利麵")#結果是"我就請你吃義大利麵"
elif message1 >=120:#假設你投入金額小於200
    print("我就請你吃泡麵")#結果是"我就請你吃泡麵"
else:
    print("你就不要吃阿白癡")#結果是"你就不要吃阿白癡""

