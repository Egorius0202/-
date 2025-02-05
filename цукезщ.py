Кононыхин Егор мф-71
import pandas as pd
df_excel = pd.read_excel('data.xlsx')
print(df_excel.head())
print(df_excel.sample(5))
print(df_excel.tail(5))
num_1=int(input("напиши номер строки"))
df_excel = pd.read_excel('data.xlsx',index_col=num_1)
print(df_excel)
22.01.2025
import pandas as pd
num_1=int(input("напиши номер строки"))
num_2=int(input("напиши номер столбца"))
df= pd.read_excel('оценка1.xlsx')
print(df)
print(df.iloc[num_1, num_2])
05.02.2025
 import math
import pandas as pd
num_1=int(input("введите 1 если вывести весь дата сэт,введите 2 вывести конкретную строчку, введите 3 вывести столбец, введите 4 вывести ячейку"))
num_2=1
num_3=2
num_4=3
num_5=4
if num_1  == num_2 :
 df_excel = pd.read_excel('Оценки (1).xlsx')
print(df_excel.head())
if num_1 == num_5 :
 num_6=int(input("напиши номер строки"))
num_7=int(input("напиши номер столбца"))
df= pd.read_excel('оценка (1).xlsx')
print(df.iloc[num_6, num_7])
