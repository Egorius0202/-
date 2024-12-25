Кононыхин Егор мф-71
import pandas as pd
df_excel = pd.read_excel('data.xlsx')
print(df_excel.head())
print(df_excel.sample(5))
print(df_excel.tail(5))
num_1=int(input("напиши номер строки"))
df_excel = pd.read_excel('data.xlsx',index_col=num_1)
print(df_excel)
