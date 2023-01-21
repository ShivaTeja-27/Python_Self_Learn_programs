# palindrome means reverse order of string or number show the same 


def pal(num):
    x = num[::-1]
    if x == num:
        print("it is palindrome!")
    else:
        print("not a palindrome")
        
#call by funtion outside

print(pal("madam"))
pal('121')
pal('shiva')
