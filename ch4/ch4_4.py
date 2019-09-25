a, b, c = 3, 5, 1
r1 = r2 = None
d = (b ** 2) - (4 * a * c)  # 求判斷式
if d > 0:  # 兩相異實根
    r1 = (-b + d ** 0.5) / (2 * a)
    r2 = (-b - d ** 0.5) / (2 * a)
    print("r1：%0.2f\nr2：%0.2f" % (r1, r2))
elif d == 0:  # 重根
    r1 = (-b + d) / (2 * a)
    print("r1：%0.2f" % r1)
else:  # 無實根
    print("無實根")
