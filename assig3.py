#1 print a tuple in reverse order.
tup= (23,56,89,78)
print(tup[::-1])
#2 find largest and smallest elements of a tuples
tup=(1,2,4,8,7)
print("largest:",max(tup),"smallest:",min(tup))

#3 convert a string to upper case
str1= "i am arshpreet"
str1= str1.upper()
print(str1)

#4 print true if the string contains all numeric characters
str2= (35,45,78,90)
print(str2.isnumeric())

#5 replace the word world with your name in the string "hello world"
str3="hello world"
str3= str3.replace("world","arsh")
print(str3)

#6 create a list with user defined inputs
lst= list(input().split())
print(lst)

#7 add the following list to above created list: ['google', 'apple','facebook','microsoft','tesla]
lst= lst+['google', 'apple','facebook','microsoft','tesla']
print(lst)

#8 count the number of time an object occurs in a list
print(lst.count('google'))          

#9 given are two dimensional arrays A and B which are# sorted in ascending order.write a program to merge them into a tuple.
#sorted array C that contains every items from array A and B
#in ascending order. [list]
A= [1,3,5,7,9]
B= [2,4,6,8,10]
C= A+B
C= sorted(C)
print(C)

#10 count even and odd numbers in that list
lst3= [1,2,3,4,5]
no_even=0
no_odd=0
for i in lst3:
     if i%2==0:
          no_even += 1
     else:
          no_odd += 1
print("count of even numbers:"+str(no_even))
print("count of odd numbers:"+str(no_odd))


#11 create a list with numbers and sort it in ascending order.
lst=[89,67,45,32,43]
print(lst)
lst.sort()
print(lst)



          
