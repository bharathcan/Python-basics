def add(a,b):#forml arguments
    c=a+b
    print(c)


add(23,4)#actual arguments are four types
#1st Position
def student(name,age):

    print(name,age)

student('bharath',20)
#2nd keyword
def student1(name,age):
    print(name,age)

student1(age=23,name='bharath')
#3rd default
def student2(name,age=18):
    print(name,age)
student2('bharath')
#4th variable length
def sum1(a,*b):

    c=a
    for i in b:
        c=c+i
    print(c)
sum1(2,1,2,3,4)
#ex2
def sum1(*b):

    c=0
    for i in b:
        c=c+i
    print(c)
sum1(2,1,2,3,4)
#one more type kwargs
def person(name,**data):
    print(name,data)
    print(name)
    for i,j in data.items():
        print(i,j)

person('bharath',age=23,city='mumbai',pn=886522)
