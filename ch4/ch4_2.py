ans = "0b"  # 使用者心中的數字
truefalse = "輸入y或Y代表有, 其它代表無 : "
print("猜生日日期遊戲,請回答下列5個問題,這個程式即可列出你的生日")

# 檢測2進位的第5位是否含1
q1 = "有沒有看到自己的生日日期 : \n" + \
     "16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31 \n"
num = (input(q1 + truefalse)).lower()
print(num)
if num == "y":
    ans += "1"
else:
    ans += "0"

# 檢測2進位的第4位是否含1
truefalse = "輸入y或Y代表有, 其它代表無 : "
q2 = "有沒有看到自己的生日日期 : \n" + \
     "8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31 \n"
num = input(q2 + truefalse).lower()
if num == "y":
    ans += "1"
else:
    num += "0"

# 檢測2進位的第3位是否含1
truefalse = "輸入y或Y代表有, 其它代表無 : "
q3 = "有沒有看到自己的生日日期 : \n" + \
     "4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31 \n"
num = input(q3 + truefalse).lower()
if num == "y":
    ans += "1"
else:
    num += "0"
# 檢測2進位的第2位是否含1
truefalse = "輸入y或Y代表有, 其它代表無 : "
q4 = "有沒有看到自己的生日日期 : \n" + \
     "2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31 \n"
num = input(q4 + truefalse).lower()
if num == "y":
    ans += "1"
else:
    ans += "0"
# 檢測2進位的第1位是否含1
truefalse = "輸入y或Y代表有, 其它代表無 : "
q5 = "有沒有看到自己的生日日期 : \n" + \
     "1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31 \n"
num = input(q5 + truefalse).lower()
if num == "y":
    ans += "1"
else:
    ans += "0"

print("生日日期是 : ", int(ans, 2))