Кононыхин Егор мф-71 сложный уровень
1:
num1=int(input("введи ширину первого паралепипида"))
num2=int(input("введи длину первого паралепипида"))
num3=int(input("введи высоту первого паралепипида"))
num4=int(input("введи ширину второго паралепипида"))
num5=int(input("введи длину второго паралепипида"))
num6=int(input("введи высоту второго паралепипида"))
num7=int(input("введи ширину третьего паралепипида"))
num8=int(input("введи длину третьего паралепипида"))
num9=int(input("введи высоту третьего паралепипида"))
print((num1*num2*num3)+(num4*num5*num6)+(num7*num8+num9))
2:
num1=int(input("введите число"))
print(num1*1)
print(num1*2)
print(num1*3)
print(num1*4)
print(num1*5)
print(num1*6)
print(num1*7)
print(num1*8)
print(num1*9)
print(num1*10)
3:
import math
C=int(input("введите С"))
k=int(input("введите k"))
n=int(input("введите n"))
print(math.factorial(n)//(math.factorial(k)*math.factorial(n-k)))
print("calkulate")

import pandas as pd

df_excel = pd.read_excel('Оценки.xlsx')

print(df_excel.head())

print(df_excel.info())
