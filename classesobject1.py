#Create a user defined dictionary
#and get keys corresponding to the value using for loop. 
dt={}
for i in range (int(input("Enter the key-value pairs you want to input:"))):
    dt[i]=i
n=int(input("Enter the value for which the key you want to search:"))
for key in dt.keys():
    if dt[key]==n:
        print(key)
    else:
        print("key not found!!! Error")
print("total elements present are:",dt[i])
print('-'*10)
#Create a dictionary and store student names and
#create nested dictionary to store the subject wise marks of every student.
#Print the marks of a given student from that dictionary for every subject. 
students={
          "arshi":{"networks":76,"python":56,"law":80,"java":40},
          "anmol":{"networks":86,"python":96,"law":90}
          }
st_name=input("Enter the name of student you want to search:").title()
if st_name in students:
    print("st_name")
    for key,value in students[st_name].items():
        print(key,value)
else:
    print("No such student in the list ")
