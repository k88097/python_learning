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
```Python
x, y = 1, 2
```
* 加法 ( + )
```Python
ans = x + y

---output---
3
```
* 減法 ( - )
```Python
ans = x - y

---output---
-1
```
* 乘法 ( * )
```Python
ans = x * y

---output---
2
```
* 除法 ( / )
```Python
ans = x / y

---output---
0.5
```
### 4. 其他的特殊運算
* 求餘數 ( % )
```Python
ans = x % y

---output---
1
```
* 求整數 ( // )
```Python
ans = x // y

---output---
0
```
* 次方 ( ** )
```Python
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
```Python
x = y = z = 10

x, y, z = 10, 20, 30
```

### 8. 刪除變數
變數刪除後，將無法再次使用，需要重新定義才可使用。
```Python
del 變數名稱

del x
```

### 9. Python的斷行
Python允許一行多個敘述，但是彼此要用";"隔開，儘管有提供此功能，也不鼓勵使用此方式撰寫程式碼。
```Python
x = 10;print(y)
```
另外也有將一個敘述拆成多行的寫法。
```Python
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

    ```Python
    #n是年
    本金和 = 本金 * (1 + 年利率) ** n
    ```
    
    你有一筆5萬元，請計算5年後的本金和。
    Ans:[解答](https://github.com/k88097/python_learning/blob/master/ch1/ch1_1.py)
    
2. 假設圓半徑是5公分，圓面積與圓周長計算公式分別如下：

    ```Python
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
    '''Python
    x = 10
    print(type(x))
    
    ---output---
    <class 'int'>
    '''