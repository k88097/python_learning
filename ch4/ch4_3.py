# 寫法一

year = eval(input("請輸入西元出生年 : "))
year -= 1900
zodiac = year % 12
if zodiac == 0:
    print("你是生肖是 : 鼠")
elif zodiac == 1:
    print("你是生肖是 : 牛")
elif zodiac == 2:
    print("你是生肖是 : 虎")
elif zodiac == 3:
    print("你是生肖是 : 兔")
elif zodiac == 4:
    print("你是生肖是 : 龍")
elif zodiac == 5:
    print("你是生肖是 : 蛇")
elif zodiac == 6:
    print("你是生肖是 : 馬")
elif zodiac == 7:
    print("你是生肖是 : 羊")
elif zodiac == 8:
    print("你是生肖是 : 猴")
elif zodiac == 9:
    print("你是生肖是 : 雞")
elif zodiac == 10:
    print("你是生肖是 : 狗")
else:
    print("你是生肖是 : 豬")

# 寫法二
year = eval(input("請輸入西元出生年：")) - 1900
list_animal = ['鼠', '牛', '虎', '兔', '龍', '蛇', '馬', '羊', '猴', '雞', '狗', '豬']
zodiac = year % 12
print("你的生肖是：%s" % list_animal[zodiac])
