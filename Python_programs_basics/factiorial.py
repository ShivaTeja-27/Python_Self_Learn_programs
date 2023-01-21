def fact(num):
    if num == 1:
        return num
    else:
        return num * fact(num - 1)


print(fact(4))

print(fact(9))

print(fact(1))
