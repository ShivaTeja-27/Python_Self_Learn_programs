year = int(input("enter the year ==> "))

if year % 400 == 0:
    print("its a leap year!!!")
elif year % 4 == 0:
    print("its a leap year!!!")
elif year % 100 == 0:
    print("its not a leap year")
else:
    print("not a leap year")


#2020 is leap year