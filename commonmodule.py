# Print the current day using Datetime module.

from datetime import date
import calendar
my_date=date.today()
print(calendar.day_name[my_date.weekday()])
print('-'*20)

#Q.2- Open your browser and play a video using webbrowser module in python.
import webbrowser
import time

total_breaks=3
break_count=0
while(break_count<total_breaks):
    print("this is program on:"+time.ctime())
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=kw4tT7SCmaY")
    break_count+=1
print('-'*20)

#Write a program to rename all the files in a directory and
#convert them into .jpg file format.
import os
path='C:/Users/R/PycharmProject/danish'
files=os.listdir(path)
i=1

for file in files:
    os.rename(os.path.join(path,file),os.path.join(path,str(i)+'.jpg'))

    i+=1
