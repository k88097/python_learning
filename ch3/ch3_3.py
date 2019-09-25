import math

s = eval(input("請輸入五邊形邊長："))
area = (5 * s ** 2) / (4 * math.tan(math.pi / 5))
print("面積：%0.2f" % area)