#Candidate-elimination algorithm

import numpy as np
import pandas as pd

#function-1
def generalize(b,a):
    for i in range(0,len(b)):
        if b[i]!=a[i]:
            b[i]='q'
        else:
            b[i]=a[i]
        
    return b

#function-2
def specialize(c,d,f):
    for i in range(0,len(c)):
        if d[i]!=f[i]:
            c[i][i]=d[i]
        else:
            c[i][i]='q'
        
    return c

#function-3
def simplify_g(g1):
  g2=[]
  o=len(g1[0])
  
  for i in g1:
    c=0
    for j in i:
      if j=='q':
        c+=1
    if c==o:
      #g1.remove(i)
      g2.append(i)

  
  g3=[]
  for i in g1:
    for j in g2:
      if i==j:
        continue
      else:
        g3.append(i)
        break

  return g3

#function-4
def len_of_s(s1):
  n=0
  for i in s1:
      if i!='q':
          n=n+1

  return n

#function-5
def len_of_g(g1):
  m=0
  for i in g1:
      for j in i:
          if j!='q':
              m=m+1  
          break 
  return m     

#function-6
def version_space(s1):
 
  s2=[]
  for i in l:
    for j in range(len(s1)):
      if s1[j]!='q':
        str1=s1[j]
        s1[j]='q'
        if len_of_s(s1)==i:
          print(s1)
          s2.append(s1)
        s1[j]=str1

  return s2

#source code

d=pd.DataFrame(pd.read_excel(r'/content/temperature.xlsx'))
print(d)

k=np.array(d)
print(k)

t=k[:,-1]
print(t)

k1=np.array(k[0:len(k),0:-1])
print(k1)

n=len(k1[0])
s=[]
for i in range(n):
  s.append(0)
print(s)
g=[]
for i in range(n):
  g1=[]
  for j in range(n):
    g1.append('q')
  g.append(g1)
print(g)

s1=s
g1=[[]]
for i in range(0,len(k1)):
    if t[i]=='yes':
        s1=generalize(s1,k1[i])
    else:
        g1=specialize(g,s1,k1[i])
    print(s1)
    print("\n")
    print(g1)
    print("\n")
    
    
s1=s
g1=[[]]
for i in range(0,len(k1)):
    if t[i]=='yes':
        s1=generalize(s1,k1[i])
    else:
        g1=specialize(g,s1,k1[i])
print(s1)
print("\n")
print(g1)
print("\n")

g1=simplify_g(g1)
print(g1)

l=[]
n=len_of_s(s1)
m=len_of_g(g1)
for i in range(m+1,n):
  l.append(i)
print(l)

s3=version_space(s1)
print(s3)
