#1.
a=3
if a<4:
    try:
         a=a/(a-3)
    except ZeroDivisionError as ob:
         print(ob)

#2
try:
    l=[1,2,3]
    print(l[3])
except IndexError as ob:
    print(ob)



#3
try:
    raise NameError("Hi There")
except NameError :
    print("an exception")
    raise

#4
def AbyB(a,b):
    try:
        c=((a+b) /(a_b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)
AbyB(2.0,3.0)
AbyB(3.0,3.0)
#5 import error
import sys
try:
    from time import datetime
except Exception as e:
    print(e)
while True:
    try:
        x=int(input("please enter a number:"))
        break
    except ValueError:
        print("that was not a valid number")
x=[92,13,76]
try:
    for i in range(5):
        print(x[i])
except IndexError as ab:
            print(ab)
    
