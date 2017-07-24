Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a +https://www.google.co.il/search?client=ubuntu&channel=fs&q=hppts%3A%2F%2Ftinyurl.com%2Fmeet2017y1csmod2&ie=utf-8&oe=utf-8&gfe_rd=cr&ei=4pV1Wa3rDI3KXriArJA
KeyboardInterrupt
>>> a = 10 b = 5
SyntaxError: invalid syntax
>>> 
KeyboardInterrupt
>>> a = 10
>>> b = 5
>>> a
10
>>> b
5
>>> a = b
>>> b = a
>>> a
5
>>> b
5
>>> a = 5
>>> b = 10
>>> a = b
>>> b
10
>>> c
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> c = a
>>> a
10
>>> 
KeyboardInterrupt
>>> a = 5
>>> b = 10
>>> c =a
>>> a
5
>>> b
10
>>> c
5
>>> a = b
>>> b = c
>>> a
10
>>> b
5
>>> c
5
>>> four = '4'
>>> print(four*3)
444
>>> five = 4
>>> print(five)
4
>>> print(five*3)
12
>>> Gilad_Segev = 'student'
>>> print("Hi," + 'Gilad_Segev')
Hi,Gilad_Segev
>>> my_name = 'student'
>>> print('Hi,' + myname')
      
SyntaxError: EOL while scanning string literal
>>> my_name = 'studnt'
>>> print('Hi,' + 'my_name')
Hi,my_name
>>> my_name = 'studnt'
>>> print('Hi,' + my_name)
Hi,studnt
>>> my_age = 15
>>> print('i am ' + my_age + 'years old')
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    print('i am ' + my_age + 'years old')
TypeError: Can't convert 'int' object to str implicitly
>>> my_age = '15'
>>> print('I am ' , my_age + 'years old')
I am  15years old
>>> score = 1
>>> total = score + (count * 2)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    total = score + (count * 2)
NameError: name 'count' is not defined
>>> score = 1
>>> count = 2
>>> total = score + (count * 2)
>>> print(total)
5
>>> 
