# 8- Prime numbers ---- a number divisible or multiplyed by 1 only are prime numbers  2, 3 , 5, 7, 11, 13, 17, 23, 29

number = int(input("enter numbers to check::: " "\n"))

for i in range(2, number):
    if number % i == 0:
        print("Not Prime number")
        break
    else:
        print("prime number found")
        break