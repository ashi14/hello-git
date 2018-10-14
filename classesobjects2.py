#classes and objects
#Create a circle class and initialize it with radius.
#Make two methods getArea and getCircumference inside this class.
class Circle():
  def __init__(self,radius):
    self.radius = radius
  def  getArea(self):
    return 3.14*self.radius*self.radius
  def getCircumference(self):
    return self.radius*2*3.14
newCircle= Circle(4)
print(newCircle.getArea())
print(newCircle.getCircumference())
print('*'*20)      
#Create a Student class and initialize it with name and roll number.
#Make methods to : 
#1. Display - It should display all informations of the student. 
#2. setAge - It should assign age to student 3. setMarks -
#It should assign marks to the student.
class Student():
  def __init__(self,name,roll):
    self.name=name
    self.roll=roll
  def display(self):
      print (self.name)
      print (self.roll)
  def age(self,age):
      self.age=age
      temp=self.age
      return temp
  def setMarks(self,marks):
      self.marks= marks
      tempy=self.marks
      return tempy
newStudent= Student('arsh',22,)
print(newStudent.display())
print(newStudent.age(20))
print(newStudent.setMarks(50))
print('*'*20)
# Create a Temprature class and create two methods: 
#1. convertFahrenheit - It will take celsius and will print it into Fahrenheit. 
#2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.      
class Temperature():
    def convertfahrenheit(self,celsius):
       return(celsius*(9/5))+32
    def convertCelsius(self,fahrenheit):
       return(fahrenheit-32)*(5/9)
newTemperature= Temperature()
print(newTemperature.convertfahrenheit(100))
print(newTemperature.convertCelsius(200))
print('*'*20)
# Create a class MovieDetails and initialize it with artistname,Year of release and ratings . 
#Make methods to 
#1. Display-Display the details. 
#2. Add- Add the movie details.
class MovieDetails():
    def __init__(self,artistname,yearofrelease,ratings):
        self.artistname=artistname
        self.yearofrelease= yearofrelease
        self.ratings= ratings
    def displaydetails(self):
        print(self.artistname)
        print(self.yearofrelease)
        print(self.ratings)
    def update(self,artistname,yearofrelease,ratings):
        self.artistname=input("enter the artist name:")
        self.yearofrelease=input("enter the year of release:")
        self.ratings=input("enter the ratings:")
        print(self.artistname,self.yearofrelease,self.ratings)
newMoviedetails= MovieDetails('vishal',2014, 4)
print(newMoviedetails.displaydetails())
print(newMoviedetails.update('haider','Shahid Kapoor',5))
print('*'*20)
#5.
class Animal():
    def __init__(self,color,legs):
      self.color=color
      self.legs=legs
    def bark(self):
      print("roar")
class Tiger(Animal):
    def bark(self):
      print("tiger roar")

if __name__=="__main__":
  pet1=Tiger("white",4)
  pet1.bark()
  print(pet1.color,",",pet1.legs)
print('*'*50)

#6
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a=A()
b=B()
print(a.f(), b.f())
print(a.g(), b.g())
print('*'*50)
#7
class shape():
  length=float()
  breadth=float()

  def arear(self,length,breadth):
    self.length=length
    self.breadth=breadth
    return self.length*self.breadth
  def areas(self,a):
    self.side=a
    return self.side*self.side
class rectangle(shape):
  def displayarea1(self):
    l=30
    b=22
    print("area of rectangle:",self.arear(l,b))
r=rectangle()
r.displayarea1()

class square(shape):
  def displayarea2(self):
    a=10
    print("area of square:",self.areas(a))
s=square()

s.displayarea2()



        
