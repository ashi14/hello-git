#q.no.1
f=open(r"arshi.txt","r")
f1=f.readlines()
for i in f1:
    print(i)
f.close()

#q.no.2
f=open(r"arshi.txt","r")
f1=f.read()
s=input("enter a word to count its occurence: ")
c=0
for i in f1:
    if i==s:
        c+=1
f.close()
print(s,"occurs",c,"times.")

#q.no.3
f=open(r"arshi.txt","r")
f1=f.read()
f.close()
f2=open(r"abc.txt","w")
f2.write(f1)
f2.close()

#q.no.4
f=open(r"arshi.txt","r")
f1=open(r"abc.txt","r+")
for i,j in zip(f,f1):
    f1.write(i+j)
f.close()
f1.close()

#q.no.5
import random
f=open(r"abc.txt","w+")
for i in range(10):
    num=random.randint(1,10)
    f.write(str(num))
f.close()
f=open("abc.txt","r")
f1=f.read()
l=[]
for i in f1:
    i=int(i)
    l.append(i)
l.sort()
f2=open(r"arshi.txt","w")
for j in l:
    f2.write(str(j))
f2.close()
f.close()
