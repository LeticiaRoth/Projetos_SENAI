import pandas as pd

df = pd.read_csv('LOPAL_Integrador.csv')
df.to_excel('Funcionalidade_Excel.xlsx', index=False)



