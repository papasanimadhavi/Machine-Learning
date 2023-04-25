import numpy as np
import pandas as pd

k=pd.DataFrame(pd.read_excel('/content/temperature.xlsx'))
print(k)

k=np.array(k)
print(k)

t=k[:,-1]
print(t)
print(k[0][0])

h=[0,0,0,0,0,0]
n=len(h)
for i in range(len(h)):
  for j in range(len(t)):
    if t[j]=='yes':
        h[i]=k[0][i]
        break
    
print(h)


for i in range(0,len(k)):
    if k[i][len(h)]=='yes':
      for j in range(0,len(h)):
          if h[j]!=k[i][j]:
              h[j]='q'
          else:
              h[j]=k[i][j]
            
print(h)

