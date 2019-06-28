def getgrade(score):
    if score>=90:
        return 'A'
    if score>=80:
        return 'B'
    if score>=60:
        return 'C'
    if score>=20:
        return 'D'
    if score==0:
        return 'F'



def main():
    score=int(input("1.enter score to get grade:"))

    score = int(input("2.enter score to get grade:"))
    print("grade is:", getgrade(score))
   # print()

main()
