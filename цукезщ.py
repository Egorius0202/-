Кононыхин Егор мф-71
import pandas as pd

df_excel = pd.read_excel('data.xlsx')

print(df_excel.info())

print(df_excel.[["column1","column2"]])
