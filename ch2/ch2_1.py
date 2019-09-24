dist = 384400                               # 地球到月球距離
speed = 1225                                # 馬赫每小時1225公里
total_hours = dist // speed                 # 計算小時數
days, hours = divmod(total_hours, 24)       # 商 = 計算天數，餘數 = 計算小時數
print("總共需要天數：%d" % days)
print("小時數：%d" % hours)