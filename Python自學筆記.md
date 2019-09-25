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
    
---
    
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

所謂的科學記號就是**把一個數字轉成數學式**表示：\\(a×10^n\\)，其中 \\(a\\) 為浮點數。

數字123456可以轉為以下型態：

$1.23456×10^5$

當然也不只有一種表示方式，也有以下的這種方式：

$1.23456E+5$

或

$1.23456e+5$

如果遇上小於1的數值，則E或e的右邊會變為負值"-"。

例如，0.000123可以用以下型態表示：

$1.23E-4$

或

$1.23e-4$

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


* **字串連接**\
數學的運算子"+"，可以執行兩個字串的相加，產生新的字串。

```python=
x = 'aaa'
y = "bbb"
z = x + y
print(z)

---output---

aaabbb
```
* 處理多一行的字串\
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

    Ans:[解答](https://github.com/k88097/python_learning/blob/master/ch2/ch2_1.py)

2. **計算坐標軸2點之間的距離**\
有2個點座標分別是(1, 8)、(3, 10)，求這2個點的距離。\
**提示：**
    1. 畢氏定理： $a^2+b^2=c^2$
    2. 兩點求一直線公式： $\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}$
    
    Ans:[解答](https://github.com/k88097/python_learning/blob/master/ch2/ch2_2.py)

---

## 第三章 基本輸入與輸出

### 1. Python的輔助說明 help()

**help()** 函數可以列出某一個Python的指定或函數的使用說明。

```python=
help(print)

---output---

Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```

### 2. 格式化輸出資料使用 print()

print()的基本語法如下：

```python=
print(value, ..., sep=' ', end="\n", file=sys.stdout, flush=False)
```

* **value**：想要輸出的值。
* **sep**：當輸出多筆資料時，可以插入各筆資料的分格字元，預設是一個空白字元。
* **end**：資料輸出結束時在最後插入的字元，預設是插入換行字元。如果不要讓輸出換行，只要輸入**end=""** 即可。
* **file**：資料輸出的位置，預設的**sys.stdout**意思是螢幕上輸出。
* **flush**：是否清除資料流的緩衝區，預設是不清除。

```python=
str1 = "111"  
str2 = "222"  
print(str1, str2)  
print(str1, str2, end="\t")     #結尾以Tab功能輸出而不是預設的換行\n  
print(str1, str2, sep=" ... ")

---output---

111 222
111 222	111 ... 222
```

### 3. 格式化 print() 輸出

格式化的基本格式如下：*(如果變數只有一個，%的後面可以不用括號)*

```python=
print("...輸出格式..." % (變數, 變數, ...))
```

輸出格式有下列幾種格式：
* **%d**：整數輸出。
* **%f**：浮點數輸出。
* **%x**：16進位整數輸出。
* **%X**：16進位大寫整數輸出。
* **%o**：8進位整數輸出。
* **%s**：字串輸出。
* **%e**：科學記號e的輸出。
* **%E**：科學記號E的輸出。

```python=
name = "品淵"  
score_python = 97  
score_java = 90  
avg = (score_python + score_java) / 2  
print("%s的成績如下：" % name)  
print("Python：%d\nJava：%d\n平均分數：%f" % (score_python, score_java, avg))

---output---

品淵的成績如下：
Python：97
Java：90
平均分數：93.5
```

### 4. 精準控制格式化輸出
為了使輸出能夠更加精準，會加上下列參數，使得輸出更加精準。

```
m：保留多少格數供輸出。
n：小數資料保留格數。
+：輸出資料是正值時，會在最左邊加上"+"符號。
-：保留格數空間有多時，資料靠左輸出。
```

* **%(+|-)nd**：整數輸出。
* **%(+|-)m.nf**：浮點數輸出。
* **%(+|-)nx**：16進位輸出。
* **%(+|-)no**：8進位輸出。
* **%(-)ns**：字串輸出。
* **%(-)m.ns**：m是字串寬度，n是顯示字串長度，n小於字串長度時會有裁減字串的效果。
* **%(+|-)e**：科學記號e的輸出。
* **%(+|-)E**：科學記號E的輸出。

```python=
x, y, s = 100, 10.5, "Python"  
print("x=/%6d/" % x)  
print("y=/%6.2f/" % y)  
print("s=/%8s/" % s)  
print("保留格數空間不足時")  
print("x=/%2d/" % x)  
print("y=/%3.2f/" % y)  
print("s=/%5s/" % s)

---output---

x=/   100/
y=/ 10.50/
s=/  Python/
保留格數空間不足時
x=/100/
y=/10.50/
s=/Python/
```

其中，**%m.ns**字串輸出最為特殊：

```python=
s = "abcdefghij"  
print("/%10.4s/" % s)

---output---

/      abcd/
```

### 5. format() 函數

Python加強版的格式化輸出，基本格式如下：

```python=
print("...輸出格式區...".format(變數,...))
```

在輸出格式區，皆以"{}"來表示。

```python=
score_python = 97  
score_java = 90  
avg = (score\_python + score\_java) / 2  
print("Python：{}\\nJava：{}\\n平均分數：{}".format(score_python, score_java, avg))

---output---

Python：97
Java：90
平均分數：93.5
```

也可以用編號來表示順序或是變數，範例如下：

```python=
score_python = 97  
score_java = 90  
avg = (score\_python + score\_java) / 2  
print("Python：{0}\\nJava：{1}\\n平均分數：{2}".format(score_python, score_java, avg))  
print("===============")  
print("Python：{p}\\nJava：{j}\\n平均分數：{a}".format(p=97, j=90, a=(97 \+ 90) / 2))

---output---

Python：97
Java：90
平均分數：93.5
===============
Python：97
Java：90
平均分數：93.5
```

在**format()** 中也可以使用精準的輸出，傳統的是使用"."來區隔，它則是使用":"，也可以選擇對齊方式。
```
>：靠右對齊
<：靠左對齊
^：置中對齊
```

```python=
r = 5  
PI = 3.14159  
area = PI * r ** 2  
print("/半徑{0:3d}圓面積是{1:10.2f}/".format(r,area))  
print("/半徑{0:>3d}圓面積是{1:>10.2f}/".format(r,area))  
print("/半徑{0:<3d}圓面積是{1:<10.2f}/".format(r,area))  
print("/半徑{0:^3d}圓面積是{1:^10.2f}/".format(r,area))

---output---

/半徑  5圓面積是     78.54/
/半徑  5圓面積是     78.54/
/半徑5  圓面積是78.54     /
/半徑 5 圓面積是  78.54   /
```

### 6. 輸出資料到檔案 open()函數

因為預設是將資料輸出至螢幕，可以利用此特性將資料輸出到指定檔案。

```python=
file_Obj = open(file, mode="r")
```

* **file**：用字串列出欲開啟的檔案，如不只名路徑則開啟目前工作資料夾。
* **mode**：開啟檔案模式，如果省略不寫預設以r模式。也同時具有多項模式，例如："wb"代表以二進位檔案開啟供寫入資料。
    * "r"：**預設**，開啟檔案供讀取。
    * "w"：開啟檔案供寫入，覆蓋原有內容。
    * "a"：開啟檔案供寫入，將新資料接在原資料後面。
    * "x"：開啟新的檔案供寫入，如果開啟已存在的檔案會產生錯誤。
    
    **下列是第二個字母意義，代表檔案類型。**
    * "b"：開啟二進位檔案模式。
    * "t"：**預設**，開啟文字檔案模式。
* **file_Obj**：檔案物件名稱，可自行命名。

另外，不使用時，一定要關閉 **"file_Obj.close()"** ，才可返回作業系統的檔案管理員觀察執行結果。

接著只要在**print()**的參數**file**中指定檔案名稱即可

```python=
print("Python is easy.", file=file_Obj)
file_Obj.colse()
```

### 7. 資料輸入 input()

input()與print()剛好相反，input()會從螢幕讀取輸入資料，但是輸入的資料回傳到程式中一定都是**字串型態**，如果要使用數學運算一定要先用int()轉成數字型態。使用格式如下：

```python=
value = input("prompt:")
```

```python=
name = input("請輸入姓名：")  
engh = int(input("請輸入英文成績："))  
math = int(input("請輸入數學成績："))  
total = engh + math  
print("%s 你的總分是 %d" % (name, total))

---output---

請輸入姓名：品淵
請輸入英文成績：93
請輸入數學成績：100
品淵 你的總分是 193
```

### 8. 處理字串的數學運算 eval()

Python中有一個非常好用的計算數學表達式的函數 **eval()**，可以直接傳回字串內數學表達式的計算結果。

```python=
number = eval(input("請輸入數學公式："))  
print("結果：%0.2f" % number)

---output---

請輸入數學公式：43/6+10
結果：17.17
```

### 9. 列出所有內建函數 dir()

可以列出指定函數中所有的函式。

```python=
print(dir(str))     #列出str()中所有函式

---output---

['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

### 10. 小試身手

1. **溫度轉換**

    請輸入華氏溫度(°F)，這個程式會輸出華氏溫度(℃)。
    
    轉換公式如下：

    $$攝氏溫度 = (華氏溫度 - 32) × 5 ÷ 9$$
        
    Ans：[解答](https://github.com/k88097/python_learning/blob/master/ch3/ch3_1.py)

2. **房貸問題**

    設計一個程式，能夠輸入貸款金額、貸款年限、年利率，程式能夠自動計算出借款人每個月需要還款的金額、總共還款金額。
    
    **提示：銀行常使用年利率，但是計算時必須以月利率才計算。**
    
    貸款問題計算公式如下：
    
    $$每個月還款金額=\dfrac{貸款金額×月利率}{1-\dfrac{1}{(1+月利率)^{貸款年限×12}}}$$
    
    Ans：[解答](https://github.com/k88097/python_learning/blob/master/ch3/ch3_2.py)

3. **正五角形面積計算**

    輸入正五角形的邊長s，此程式會計算此五角形的面積，面積取到小數下兩位。
    
    面積計算公式如下：
    
    $$area=\dfrac{5×s^2}{4×tan(\dfrac{π}{5})}$$
    
    Ans：[解答](https://github.com/k88097/python_learning/blob/master/ch3/ch3_3.py)

4. **計算經緯度距離**

    香港紅磡車站的經緯度是(25.0452929, 121.5168704)，台北車站的經緯度是(22.2838912, 114.173166)，請計算兩者之間的距離，距離計算到小數下兩位。
    
    經緯度求距離公式如下：
    
    $$distance=r×acos(sin(x_1)×sin(x_2)+cos(x_1)×cos(x_2)×cos(y_1-y_2))$$
    
    Ans:[解答](https://github.com/k88097/python_learning/blob/master/ch3/ch3_4.py)
    
---

## 第四章 程式的流程控制 if 敘述

### 1. 關係運算子


| 關係運算子 | 實例 | 說明 |
| :--------: | :--------: | -------- |
|>|a > b|檢查a是否大於b|
>=|a >= b|檢查a是否大於或等於b
<|a < b|檢查a是否小於b
<=|a <= b|檢查a是否小於或等於b
==|a == b|檢查a是否等於b
!=|a != b|檢查a是否不等於b

如果上述的運算成立，會回傳 **True**，否則會回傳 **Flase**。

### 2. 邏輯運算子

* **and**：相當於邏輯符號 AND
* **or**：相當於邏輯符號 OR
* **not**：相當於邏輯符號 NOT

    下表為 and 的邏輯運算：

    |and|True|False|
    |-|-|-|
    |**True**|True|False|
    |**False**|False|False|

    下表為 or 的邏輯運算：

    |or|True|False|
    |-|-|-|
	|**True**|True|True|
	|**False**|True|False|

	下表為 not 的邏輯運算：

	|not|True|False|
	|-|-|-|
	|||False|True|
    
### 3. if 敘述

if 敘述的基本語法：

```python=
if (判斷條件):        #條件外的小括號可有可無
    程式碼區塊
```

如果判斷條件為 **True** 時，則執行程式碼區塊，否則不執行。如果程式碼區塊只有一行程式碼，可以減寫成以下格式：

```python=
if 判斷條件 : 程式碼區塊
```

※**注意**，Python是使用**內縮方式**區隔程式碼區塊，如果沒有標準的排版習慣的話很容易造成程式執行錯誤。

```python=
age = int(input("請輸入年齡："))  
if age < 18:  
    print("你未滿18歲，不得喝酒。")

---output---

請輸入年齡：17
你未滿18歲，不得喝酒。
```

### 4. if...else 敘述

這段的敘述很像我們中文的，**假如...，否則就...**。

語法如下：

```python=
if 條件判斷:
    程式碼區塊
else:
    程式碼區塊
```

範例如下：

```python=
num = int(input("輸入一個整數："))  
if num % 2 == 0:  
    print("%d 是偶數。" % num)  
else:  
    print("%d 是奇數。" % num)

---output---

輸入一個整數：100
100 是偶數。
```

### 5. if...elif...else 敘述

如果只有if..else會不滿足需求，這時候就可以使用這個敘述。

語法如下：

```python=
if 條件判斷:
    程式碼區塊
elif 條件判斷:
    程式碼區塊
else:
    程式碼區塊
```

範例如下：
```python=
score = int(input("輸入分數："))  
if score < 60:  
    print("不及格")  
elif score >= 90:  
    print("很棒")  
else:  
    print("尚可")

---output---

輸入分數：95
很棒
```

### 6. 巢狀 if 敘述

所謂的巢狀 if 敘述就是指說 if 當中還有一個 if 敘述。
```python=
if 判斷條件:
    if 判斷敘述:
        程式碼區塊
    else:
        程式碼區塊
else:
    程式碼區塊
```

範例如下：

```python=
print("判斷輸入年份是否潤年")  
year = input("請輸入年分: ")  
rem4 = int(year) % 4  
rem100 = int(year) % 100  
rem400 = int(year) % 400  
if rem4 == 0:  
    if rem100 != 0 or rem400 == 0:  
        print("%s 是潤年" % year)  
    else:  
        print("%s 不是潤年" % year)  
else:  
    print("%s 不是潤年" % year)

---output---

判斷輸入年份是否潤年
請輸入年分: 2019
2019 不是潤年
```

### 7. 未設定的變數值 None

有些人設計程式，喜歡先將變數先宣告，在還沒用到這個變數，它的值都是 **None**。

```python==
x = None  
print(x)  
print(type(x))

---output---

None
<class 'NoneType'>
```

### 8. 小試身手

1. **BMI程式**

    這個程式會要求輸入身高與體重，然後計算BMI指數，由這個指數判斷體重是否正常。
    
    BMI公式如下：
    
    $$BMI=\dfrac{體重_{(Kg)}}{身高^2_{(m)}}$$
    
    Ans：[解答]()
    
2. **猜出生日期**

    寫一隻程式可以，此程式可以透過問使用者五個問題，問完即可猜出使用者的出生日期。
    
    提示：一個月份最多有31天，5個問題，每次回答是跟否。$2^5=32$
    
    Ans：[解答]()
    
3. **12生肖系統**

    請輸入你出生的西元年，程式會輸出相對應的生肖。
    
    Ans：[解答]()
    
4. **求一元二次方程式的根**

    有一個一元二次方程式如下：
    
    $$3x^2+5x+1=0$$
    
    求根的公式如下：
    
    $$r=\dfrac{-b±\sqrt{b^2-4ac}}{2a}$$
    
    Ans:[解答]()
    
---
