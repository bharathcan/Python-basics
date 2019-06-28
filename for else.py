x=[12,23,34,66,50]

for i in x:
    if i % 5==0:
        print(i)
        break
    else:
        print("not found")


x=[12,23,34,66]

for i in x:
    if i % 5==0:
        print(i)
        break
else:
    print("not found")
