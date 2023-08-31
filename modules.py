Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d={"r":0161213, "t":0192827,"L":0171973}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
d={"r":161213, "t":192827,"L":171973}
d
{'r': 161213, 't': 192827, 'L': 171973}
{'r': 161213, 't': 192827, 'L': 171973}
{'r': 161213, 't': 192827, 'L': 171973}
d
{'r': 161213, 't': 192827, 'L': 171973}
import calendar
cal=calendar(1996,8)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    cal=calendar(1996,8)
TypeError: 'module' object is not callable
cal= calendar.month(1996,8)

print(cal)
    August 1996
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31

>>> cal=calendar(1995,8)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    cal=calendar(1995,8)
TypeError: 'module' object is not callable
>>> cal= calendar.month(1995,8)
>>> print(cal)
    August 1995
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31

>>> cal= calendar.month(1994,8)
>>> print(cal)
    August 1994
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31

>>> cal= calendar.month(1997,8)
>>> print(cal)
    August 1997
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31

