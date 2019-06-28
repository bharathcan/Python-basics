#function returning value
def max(n1,n2):
    if n1>n2:
        result=n1
    else:
        result=n2

    return result
def main():
    i=10
    j=3
    k=max(i,j)
    print("the larger number of",i,"and",j,"is",k)

main() #calling main function
