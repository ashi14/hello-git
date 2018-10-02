#determine whether the year is leap year or not.
a=int(input("enter the no:"))
if(a%4==0):
    print("the year is a leap year")
else:
    print("the year is not a leap year")

#take length and breadth and check whether the dimensions are of square/rectangle.
l= int(input( "enter the length"))
b= int(input("enter the breadth"))
if(l==b):
    print("the dmensions are of square")
else:
    print("the dimensions are of rectangle")

#take the input age of 3 people and determine the oldest and youngest.
x=45;
y=24;
z=14;
if x>=y and x>=z:
    print(x,"person is oldest")
elif y>=x and y>=z:
    print(y,"person is oldest")
elif z>=x and z>=y:
    print(z,"person is oldest")
else:
    print("all are equal")


#Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
a= int(input("enter the age :"))
g= input("enter the gender(M or F):")
m= input("enter the marital status(Y or N):")
if(g=="F")and (20<a<60):
    print("the employee will work in urban area only")
elif (g=="M")and (20<a<40):
    print("the employee can work anywhere")
elif( g=="M")and (40<a<60):
    print("the employee works in urban area only")
else:
    print("!!! error !!!")
print('-'*50)
#A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
#Ask user for quantity Suppose, one unit will cost 100.
#Judge and print total cost for user.
q=int(input("enter the quantity of product"))
if(q*100)>1000:
    print("the user gets 10% discount")
    print("total cost :",((q*100)-.1*q*100))
else:
    print("user gets no discount")
print('-'*50)

#loops
#take 10 integers from users and print it on screen.
sum=[]
for i in range(10):
    x=int(input("enter the no:"))
    sum.insert(i,x)
    i++1
print(sum)
print('-'*50)
#write an infinite loop.
while True:
    print("infinite")
print('-'*50)
#create a list of integer elements by user input,
#make a new list which will store square of elements of previous list.
m= list(map(int,input().split()))
m_square = []
for i in 1:
     m_square.append(i**2)
print(m_square)
print('-'*50)
#From a list containing ints, strings and floats,
#make three lists to store them separately
n= ["hello",1,2,3,4,.9,.8,"world"]
n_int =[]
n_float =[]
n_string =[]
for i in n:
    if(type(i)==int:
       n_int.append(i)
    elif type(i)==float:
       n_float.append(i)
    else
       n_string.append(i)
print(n_int)
print(n_float)
print(n_string)
       
#Using range(1,101), make a list containing only prime numbers.
num= []
for i in range(1,101):
       flag= false
       for j in range(2,i):
           if i%j==0:
             flag = true
       if not flag:
           num.append(i)
print(num)

#: print the star pattern
def printstar(symbol,n):
    count=1
    while count<=n:
        print(symbol*count)
        count=count+1
    return
printstar('*',5)
       
#  Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found.
#Iterate over list using for loop.
l= list(map(int.input("enter list elements:").split()))
element= int(input("enter the element to searchL:"))
if element in l:
       print("element found:")
       del.l[l.index(element)]
print(l)




