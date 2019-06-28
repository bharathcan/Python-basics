#1 case
a=20

def values():
    a=100
    print('local value',a)
values()
#2nd case
a=20

def values():
    a=100

values()
print('global value',a)
#3rd case
a=20

def values():
    a=100
    print('local value',a)
values()
print('global value',a)
#4th case
a=20

def values():

    print('local value',a) #takes global value when no local values is given but local values can't be called outside function
values()
print('global value',a)
#5th case
a=20
