def is_leap(year):
    leap = False
    
   
    if year % 4 == 0:
        if year % 400 == 0 or year % 100 != 0:
            leap = True
    
    return leap



print("enter the year :")
year = int(input())

a = int(input("no to divide :"))
b = int(input("2nd no: "))


print(a // b)
d = a / b
print("wiz floating point :" + str(d))





def check(leap):
    if leap == True:
        print("leap")
    else:
        print("not leap")

