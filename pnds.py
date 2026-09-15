import pandas as pd
import numpy as np

data = np.array(['g', 'e', 'e', 'k', 's'])
s = pd.Series(data)
print(s)

v = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(v['b'])   # 20 — access by label, not just position

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

df = pd.DataFrame(mydataset)
print(df)

df = pd.DataFrame()   # empty DataFrame
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']
df = pd.DataFrame(lst)  # single unnamed column, default integer index
print(df)