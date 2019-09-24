# Python自學筆記
 

## 第一章 認識變數與基本數學運算

### 1. 程式的註解
1. 單行註解：#註解
2. 多行註解：'''註解'''

### 2. 變數的命名
1. 系統關鍵字不可當變數名稱。   [(關鍵字列表)](https://www.programiz.com/python-programming/keyword-list)
2. 內建的函數名稱不建議當作變數名稱。  eg. abs,all..

### 3. 四則運算
四則運算是指加( + )、減( - )、乘( * )、除( / )
```python=
x, y = 1, 2
```
* 加法 ( + )
```python=
ans = x + y

---output---

3
```
* 減法 ( - )
```python=
ans = x - y

---output---

-1
```
* 乘法 ( * )
```python=
ans = x * y

---output---

2
```
* 除法 ( / )
```python=
ans = x / y

---output---

0.5
```
### 4. 其他的特殊運算
* 求餘數 ( % )
```python=
ans = x % y

---output---

1
```
* 求整數 ( // )
```python=
ans = x // y

---output---

0
```
* 次方 ( ** )
```python=
ans = x ** y

---output---

1
```
### 5. 運算的優先順序
運算時的優先順序如下：
1. 次方。
2. 乘法、除法、求餘數、求整數，彼此依照出現順序運算。
3. 加法、減法，彼此依照出現順序運算。

### 6. 指派運算子
常見的運算子如下：

|運算子|實例|說明|
| -------- | -------- | -------- |
| +=       | a += b   | a = a + b|
|-=|a -= b|a = a - b|
|= |a = b|a = a  b|
|/=|a /= b|a = a / b|
|%=|a %= b|a = a % b|
|//=|a //= b|a = a // b|
|**=|a **= b|a = a ** b|

### 7. 等號的多重指定使用
使用Python時，可以一次設定多個變數等於某一個數值。
```python=
x = y = z = 10

x, y, z = 10, 20, 30
```

### 8. 刪除變數
變數刪除後，將無法再次使用，需要重新定義才可使用。
```python=
del 變數名稱

del x
```

### 9. Python的斷行
Python允許一行多個敘述，但是彼此要用";"隔開，儘管有提供此功能，也不鼓勵使用此方式撰寫程式碼。
```python=
x = 10;print(y)
```
另外也有將一個敘述拆成多行的寫法。
```python=
a = b = c = 10

#續行方法1
x = a +\
    b +\
    c
print(x)

#續行方法2
y = (a +
     b +
     c)
print(y)
```
### 10. 小試身手
1. 銀行存款複利的計算，假設目前銀行年利率是1.5%，複利公式如下：

    ```python=
    #n是年
    本金和 = 本金 * (1 + 年利率) ** n
    ```
    
    你有一筆5萬元，請計算5年後的本金和。\
    Ans:[解答](https://github.com/k88097/python_learning/blob/master/ch1/ch1_1.py)
    
2. 假設圓半徑是5公分，圓面積與圓周長計算公式分別如下：

    ```python=
    #Pi = 3.14159, r是半徑
    圓面積 = Pi * r * r
    圓周長 = 2 * Pi *r
    ```
    Ans:[解答](https://github.com/k88097/python_learning/blob/master/ch1/ch1_2.py)
    
## 第二章 Python的基本資料型態
Python的基本資料型態有下列幾種：
* 數值：整數( int )、浮點數( float )、~~複數~~( complex number 不常用)。
* 布林值( Boolean )：也可以歸為數值型態(0,1)。
* 文字序列( text sequence type )：也就是字串( string )。
* 字元組( byte )：二進位資料型態，長度8bit。
* 序列：list、tuple。
* 對映：dict。
* 集合：set、frozenset。
### 1. type() 函數
可以利用此函數得知該變數的資料型態

```python==
x = 10
print(type(x))
    
---output---

<class 'int'>
```

### 2. 整數與浮點數的運算
Python具有簡單的自動轉換能力，在計算時會將整數轉換為浮點數再計算。

```python==
x = 10  
print(x)  
print(type(x))    #辨別x的型態
x += 5.5  
print(x)  
print(type(x))    #再次辨別x的型態

---output---

10
<class 'int'>
15.5
<class 'float'>
```
### 3. 位元數的轉換
* 2進位與bin()
可以利用bin()函數將一般數字轉成2進位。

```python=
x = 0b1101  #2進位整數
print(x)  
y = 13      #10進位整數
print(bin(y))

---output---

13
0b1101
```

* 8進位與oct()
可以利用oct()函數將一般數字轉成8進位。
```python=
x = 0o57        #8進位整數
print(x)  
y = 47          #10進位整數
print(oct(y))    #轉換為8進位

---output---

47
0o57
```

* 16進位與hex()
可以利用hex()函數將一般數字轉成16進位。
```python=
x = 0x5D      #16進位整數
print(x)  
y = 93          #10進位整數
print(hex(y))

---output---

93
0x5d
```

### 4. 強制資料型態的轉換
* int(x)：強制將x轉成整數型態。
* float(x)：強制將x轉成浮點數型態。
* str(x)：強制將x轉成字串型態。

```python==
x = 10  
print(type(x))            #判別x的型態
print(type(float(x)))     #判別x的型態
print(type(str(x)))       #判別x的型態

---output---

<class 'int'>
<class 'float'>
<class 'str'>
```
### 5. 數值運算常用的函數
* abs(x)：計算x的絕對值。
* pow(x, y)：返回x的y次方。
* round(x, y)：x=處理數，y=處理位數(無填寫則為默認小數下第0位)。如果處理位數左邊為奇數，則使用四捨五入；如果左邊為偶數，則使用五捨六入。\
`round(1.5) = 2, round(2.25, 1) = 2.2`
```python==
print("---abs()應用---")  
x, y = 10, -10  
print("x -> %d, y -> %d" % (abs(x), abs(y)))  
  
print("---pow()應用---")  
x, y = 5, 2  
print("%d 的 %d 次方為 %d" % (x, y, pow(x, y)))  
  
print("---round()應用---")  
print(round(1.5))  
print(round(2.25, 1))

---output---

---abs()應用---
x -> 10, y -> 10
---pow()應用---
5 的 2 次方為 25
---round()應用---
2
2.2
```

### 6. 科學記號表示法
所謂的科學記號就是**把一個數字轉成數學式**表示：\\(a×10^n\\)，其中 \\(a\\) 為浮點數。\
數字123456可以轉為以下型態：
$1.23456×10^5$
當然也不只有一種表示方式，也有以下的這種方式：
$1.23456E+5$
或
$1.23456e+5$
如果遇上小於1的數值，則E或e的右邊會變為負值"-"。\
例如，0.000123可以用以下型態表示：
$$1.23E-4$$
或
$$1.23e-4$$
```python=
x = 1.23456e+5  
print(x)  
y = 1.23e-4  
print(y)

---output---

123456.0
0.000123
```

### 7. 布林值資料型態
布林值( Boolean )主要的值有兩種，True或False，它的資料型態代號為bool，主要是應用在程式流程的控制，特別是在條件運算式( if )中。
```python=
x = True
print(type(x))
y = False
print(type(y))

---output---

<class 'bool'>
<class 'bool'>
```
布林值是可以轉成整數的，直接使用int()強轉即可。
```python=
x = True
print(int(x))
y = False
print(int(y))

---output---

1
0
```
此外在程式設計中False值不一定是要經過某個條件判斷是Flase才可得到False，下列情況也會視為Flase：
1. 布林值 Flase
2. 整數 0
3. 浮點數 0.0
4. 空字串 ''
5. 空串列 []
6. 空元組 ()
7. 空字典 {}
8. 空集合 set()
9. None

###  8. 字串資料型態
字串意指**兩個單引號**(')或是**兩個雙引號**(")之間的任一個數字元的資料，它的資料型態代號為str。在英文中的縮寫常常使用到單引號，如果遇到此種情況，就可以使用雙引號來解決。

* **字串輸出**
```python=
x = 'Python'
print(x)
y = "This's a book."
print(y)

---output---

Python
This's a book.
```


* **字串連接**

數學的運算子"+"，可以執行兩個字串的相加，產生新的字串。
```python=
x = 'aaa'
y = "bbb"
z = x + y
print(z)

---output---

aaabbb
```
* 處理多一行的字串

如果一段字串長度多於一行，此時就必須使用**三個單引號**( ''' )將字串包夾。另外如果要將此字串不斷行的話再行末加入 **( \ )** 即可。

```python=
str1 = '''123456
789'''
print(str1)         #字串內沒有\
str2 = '''123456\
789'''
print(str2)         #字串內有\

---output---

123456
789
123456789
```
* **逸出字元 (跳脫字元)**\
在字串中有一些特殊字元，例如：單引號、雙引號…，必須在特殊字元前面加上**反斜線**( \ )，含有這樣符號的字元通稱為**逸出字元(跳脫字元)**。

|逸出字元|意義|逸出字元|意義|
| ------ | -- | ------- | ---|
|\\'|單引號|\n|換行|
|\\"|雙引號|\o|8進位表示|
|\ \\|反斜線|\r|游標值至最左|
|\a|響鈴|\x|16進位表示|
|\b|BackSpace鍵|\t|Tab鍵|
|\f|換頁|\v|垂直定位|
* **字串與整數的互換**\
之前有提到過，str()與int()有強制轉換的功能，字串與數字的轉換也都是靠它們。
```python=
num1 = "222"  
num2 = "333"  
num3 = num1 + num2  
print("這是字串相加：", num3)  
  
num3 = int(num1) + int(num2)  
print("這是數字相加：", num3)

---output---

這是字串相加： 222333
這是數字相加： 555
```
* **字串與整數相乘的複製**\
在Python中可以允許將字串與整數相乘，結果是字串將重複該整數的次數。
```python=
x1, n = "A", 5  
print(x1)  
print(x1 * n)

---output---

A
AAAAA
```
* **逸出字元的使用與防止逸出字元執行**\
我們可以利用以下方法達到使用逸出字元的使用與防止逸出字元執行的方法：
```python=
str1 = "Python\\nis\\neasy"  
print(str1)  \# 使用逸出字元  
str2 = r"Python\\nis\\neasy"  
print(str2)  \# 不執行逸出字元

---output---

Python
is
easy
Python\nis\neasy
```
* **字串與字元**\
因為在Python中沒有所謂的字元資料，如果字串中包含字元，我們稱這是含一個字元的字串。\
常用函數如下：
    * **chr(x)** : 傳回x值的ASCII碼或Unicode碼。
    * **ord(x)** : 傳回ASCII碼的10進位值，也可傳回中文的Unicode碼。
1. **ASCII碼**\
在ASCII表中，是用8個位元定義一個字元，所以使用了0 - 127定義128個字元，每一個字元都有專屬的編號，這些編號簡稱ASCII碼。
```python=
x = 97  
y = 'a'  
print(chr(x))  
print(ord(y))

---output---

a
97
```
2. **Unicode碼**\
因為ASCII對於英文語系國家相當好用，但是對於其他國家會不友善，會有許多字無法呈現，為了讓全球都能夠使用，因此有了Unicode碼的設計。\
目前Unicode使用16位元定義，相當於定義了65536個字元，它的定義方式是以"\u"開頭後面有4個16進位的數字，所以從"\u0000"至"\uFFFF"之間。
```python=
x1 = 97  
x2 = chr(x1)  
print(x1)  
print(x2)  
x3 = "趙"  
print(hex(ord(x3)))  \# 因為ord出來是10進位，必須還要轉成16進位。

---output---

97
a
0x8d99
```
3. **utf-8編碼**\
utf-8是針對Unicode字符集的**可變長度編碼方式**，這是網際網路木其所遵循的編碼方式。utf-8使用1-4個byte表示一個字符，這種編碼方式會根據不同的字符變化編碼長度。
### 9. byte資料

|編碼|說明|
|---|---|
|ASCII|標準7位元的ASCII編碼|
|UTF-8|Unicode可變長度編碼，這也是最常使用的編碼|
|CP-1252|一般英文Windows作業系統的編碼|
|CP950|繁體中文Windows作業系統編碼|
|Unicode-Escape|Unicode的常數格式，\uxxxx或\Uxxxxxxxx|
* 字串轉成byte資料
```python=
string = "趙品淵"  
stringByte = string.encode('utf-8')  
print(stringByte)

---output---

b'\xe8\xb6\x99\xe5\x93\x81\xe6\xb7\xb5'
```
* byte資料轉成Unicode字串
```python=
string = b'\\xe8\\xb6\\x99\\xe5\\x93\\x81\\xe6\\xb7\\xb5'  
stringUcode = string.decode('utf-8')  
print(stringUcode)


---output---

趙品淵
```
### 10. 小試身手
1. **地球到月球時間計算**\
從地球到月球約是384400公里，假設火箭的速度是一馬赫，設計一個程式計算需要多少天、多少小時才可抵達月球。這個程式省略分鐘數。

    Ans:[解答](https://)

2. **計算坐標軸2點之間的距離**\
有2個點座標分別是(1, 8)、(3, 10)，求這2個點的距離。\
**提示：**
    1. 畢氏定理： $a^2+b^2=c^2$
    2. 兩點求一直線公式： $\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}$
    
    Ans:[解答](https:// "title")
