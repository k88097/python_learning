height = float(input("請輸入身高(公分)："))
weight = int(input("請輸入體重(公斤)："))
bmi = weight / ((height / 100.0) ** 2)

if bmi >= 18.5 and bmi < 24:
    print("BMI: %0.2f，體重正常" % bmi)
else:
    print("BMI: %0.2f，體重不正常" % bmi)
