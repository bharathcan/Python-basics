def update(set):
    print(set)
    print(id(set))
    set[1]=34
    print(set)
    print(id(set))


set=[12,45,78]
print(set)
print(id(set))
update(set)
print(set)
print(id(set))
