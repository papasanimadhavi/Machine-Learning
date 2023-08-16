#2 candidate -elimination alg
import numpy as np
import pandas as pd
df=pd.read_csv(r'C:\Users\hp\OneDrive\Desktop\ENJOYSPORT.csv')
print(df)

concepts=np.array(df.iloc[:,0:-1])
target=np.array(df.iloc[:,-1])

def learn(concepts,target):
    s=concepts[0].copy()
    
    g=[['?' for i in range(len(s))] for i in range(len(s))]
    
    for i,h in enumerate(concepts):
        
        if target[i]==1:
            
            for x in range(len(s)):
                if h[x]!=s[x]:
                    g[x][x]='?'
                    s[x]='?'
        if target[i]==0:
            for x in range(len(s)):
                if h[x]!=s[x]:
                    g[x][x]=s[x]
                else:
                    g[x][x]='?'
    
    indices=[i for i,val in enumerate(g) if val==['?','?','?','?','?','?']]
    for i in indices:
        g.remove(['?','?','?','?','?','?'])
        
    return s,g

s_final,g_final=learn(concepts,target)
def version_space(s,g):
    vs=[]
    for i in g:
        for j in range(len(i)):
            if i[j]=='?' and s[j]!='?':
                m=i[:]
                m[j]=s[j]
                if m not in vs:
                    vs.append(m)
    return vs

r=[]
r.append(s_final)
r1=version_space(s_final,g_final)
r.append(r1)
r.append(g_final)
print("Specific hypothesis:",s_final)
print("General Hypothesis:",g_final)
print("Version_space",r)
