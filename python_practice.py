# -*- coding: utf-8 -*-
"""Python_practice.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yvq6zXLd7WZ4G7a5PCmJm0ygRmDhQRpH
"""

print("hello world")





type(23)

'hello world 1'

"hello world 2"

"12"+"3"

2**3

y="tree"
print(y)

type(True)
type('True')

"hi" < "helloo"

"hel" < "hello"

g_list=["a","b","c","d","e","f",5]
for a in g_list:
  print(a)

(range(len(g_list)))

for i,a in enumerate(g_list):
  print(i,a)

merged=""
w1=len("abc")
w2=len("ef")
l=min(w1,w2)
print(l)
for i in range(l):
 merged += w1[i] + w2[i]
 print(merged)

word1="abc"
        word2="efg"

        merged = ""
        w1 = len(word1)
        w2 = len(word2)
        l = min(w1, w2)
        for i in range(l):
            merged += word1[i] + word2[i]
        if w1 == w2:
            return merged
        elif w1 > w2:
            return merged + word1[l:]
        elif w1 < w2:
            return merged + word2[l:]

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = ""
        w1 = len(word1)
        w2 = len(word2)
        l = min(w1, w2)
        for i in range(l):
            merged += word1[i] + word2[i]
        if w1 == w2:
            return merged
        elif w1 > w2:
            return merged + word1[l:]
        elif w1 < w2:
            return merged + word2[l:]

a=[1,2,3,4]
b=a
b

a is b

a is [1,2,3,4]

a=2
b=3
c=a
a=b
b=c
print(a,b)

a

from copy import deepcopy
a=[1,2,3,4]
b=deepcopy(a)
a is b

a=[1,2,3]

print(a)
b=a
a[0]=0
a is b
print(b)
print(a)
b[0]=9
a

def square(a):
  a=[1,3]
  return a

square(9)

def square(a):
  a=[1,3]
  a.append(0)
  return b
x=[5,6,7]
b=x.append(8)
print(x)
square(b)

p='test.txt'
with open(p,'r') as f:
  for line in f:
    print(f.readlines())

with open ('new_file.txt','a') as f:
  f.write('hello world\nthe end')

with open(p,'r') as f:
  print(f.read())

l=[1,2,3]
l.append(4)
l

l.insert(0,'hi')
l

l.count('hi')

l.reverse()
l

l.remove('hi')
l

l=[]
for i in range(5):
  for j in range(3):
    if (i+j)%2==0:
      l.append(i+j)
print(l)

d={'apple':"fruit",'ball':"playtoy"}
d

d["apple"]

d["ball"]="toy"
d

del d['apple']
d

d['cucumber']="vegetable"

d

d['gauva']='fruit'
for k in d.keys():
  v=d[k]
  print(k,v)

name="Nivi"
f"hey {name} how is it going?"

"hey {} how is it going?".format(name)

for c in "Nivi":
  print(type(c))

help("")

"my name is nivi".split(" ")

"nivi".isnumeric()

"234".isnumeric()

"1g3".isnumeric()

"hello there".upper()

"hello there".capitalize()

s="HELLO"
s[0]

for i in range(len(s)):
  print(i,s[i])

len(s)

sorted([9,2,1,7,3,5])

{1,5,2,4,2,3,5}

set('Nivi goes to a nine neon party' )

result=int(input("enter a number"))
print("The result is ", result)

result=input("enter a number")
print(f"The result is {result}")

l=[x for x in range(10)]
l

l=[x**2 for x in range(10)]
l

l=[x for x in range(5) if (x%2==0)]
l

l=[x if (x%2==0) else 'null' for x in range(5) ]
l

[0]*5

[1,5]+[9,0,3]

for a,b in zip(range(6),range(4,9)):
  print(a,b)

[(a,b)for a,b in zip(range(6),range(4,8))]

[{a:b}for a,b in zip(range(6),range(4,8))]

[(a*b)for a,b in zip(range(6),range(4,8))]

{a:b for a,b in zip(range(6),range(4,8))}

chr(65)

chr(97)

ord('a')

{k:chr(k+64) for k in range(1,27)}

{k:chr(k) for k in range(65,105)}

from copy import deepcopy
a=[1,2,3,4]
b=deepcopy(a)
b

import copy as cp
a=[1,2,3,4,[5,[0],9,6]]
b=cp.deepcopy(a)
c=cp.copy(a)
print('a=',a)
print('b=',b)
print('c=',c)

import numpy as np
a=np.array([1,2,3])
a

!pip list

!python test.py

!python test.py