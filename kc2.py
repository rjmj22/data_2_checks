import pandas as pd
data = pd.read_csv('D:\\coding\\knowledge check 2\\data.csv')
# filled in NaN with "N/A"
data = data.fillna('N/A')
# changed a mispelled column name
data.rename(columns = {'Edit' : 'Editor'}, inplace = True)
print(data)
