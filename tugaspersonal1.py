# -*- coding: utf-8 -*-
"""TugasPersonal1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1189WcHy22B1HedH6KKbAG3t6hX0QFw-Q
"""

print('hello, world!')

length = 10
width = 2
name = "saturnus"

def greeting (name):
  return 'hello,' + name

print(greeting('tere'))

a = 10
b = 30.0
a + b

print(1<10)

print("Linux" == "Windows")

print(1 != "1")

x = 7

while x > 0:
  print("positive x=" + str(x))
  x = x - 1

print("now x=" + str(x))

for x in range (3):
  print("x=" + str(x))

#break
for x in range(3):
  print('x=' + str(x))
  if x == 1:
    break

#continue
for x in range(3, 0, -1):
  if x % 2 == 0:
    continue
  print(x)

length = 10
width = 2
area = length * width

x = 10
y = 2
a = x*y

#Data Struktur List
paths = ['ML', 'Cloud']

print(paths[0])

paths.append('Android')
paths.remove('Cloud')
paths.insert(1, 'Mobile')
paths.pop(-1)

#Dictionary
students = {
    'ml': 500,
    'mpbile' : 700,
    'cloud' : 900
}

print(students['cloud'])

students['ml'] = 1000