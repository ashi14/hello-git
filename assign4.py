#1. reverse the whole list using list methods.

lst=[90,78,'perl','java',54]
lst.reverse()
print(lst)

#2 print all the upper case letters from a string.

s= 'Earth Is a Beautiful planet'
for i in s:
    if i==i.upper():
        print(i,end="")
print()

#3 split the user input using comma's and store the values in a list as integers
a=input("enter the numbers:")
print(a.split())


#4 check whether the string is palondromic or not
a=input("enter the string")
if (a==a[::-1]):
    print(a,'is a pallindrome')
else:
     print(a,'is not a pallindrome')

#5 Make a deepcopy of a list and write the difference between shallow copy and deep copy.
a=['perl',34,'java','ruby']
b=a #shallowcopy
print("original list a:",a,"id=",id(a))
print("shallow copy list b:",b,"id=",id(b))
dela[-1]
print("original list a:",a)
print("shallow copy list b:",b)

a=['perl',34,'java','ruby']
c=a.copy() #deepcopy
print("original list:",a,"id=",id(a))
print("deep copy list:",c,"id=",id(c))

del[-1]
print("original copy a:",a)
print("deep copy list c:",c)


