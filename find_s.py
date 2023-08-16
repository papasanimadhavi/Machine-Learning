#1 find-s 
import numpy as np
import pandas as pd

df=pd.read_csv(r'C:\Users\hp\OneDrive\Desktop\ENJOYSPORT.csv')
print(df)

h=["","","","","",""]
for index,row in df.iterrows():
    ind=0
    if row['EnjoySport']==1:
        for i in range(len(row)-1):
            if h[ind]=='?':
                ind+=1
                continue
            elif h[ind]==row[i]:
                ind+=1
                continue
            elif h[ind]=="":
                h[ind]=row[i]
            elif h[ind]!=row[i]:
                h[ind]='?'
            ind+=1
            
print(h)
