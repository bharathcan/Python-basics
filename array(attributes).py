from array import *
vals=array('i',[1,7,3,4,5,8,9])
newArr = array(vals.typecode,(a*a for a in vals))

print(vals)
print(vals.buffer_info())
vals.reverse()
print(vals[0])
for i in range(5):
   print(vals[i])
for i in range(len(vals)):
   print(vals[i])
for e in newArr:
    print(e)
