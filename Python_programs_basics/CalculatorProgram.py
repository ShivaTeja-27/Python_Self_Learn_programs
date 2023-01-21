def add(a, b):
    return a + b

def multi(a , b):
    return a * b

def divide(a, b):
    return a / b

def sub(a, b):
    return a - b

def  si(p, r, t):  # simple intrest 
    return (p * r * t) / 100

def ci(P, R, T):
    return P * pow((1 + R/100), T)

def sqr(num):
    return num**2

def st(num):
    return num ** 0.5

# /////////////////////////////////////////call the functions now

print(add(2,3))
print(multi(2,3))
print(divide(2,3))
print(sub(2,3))

print(si(2,3,7))
print(ci(2,3,8))

print(sqr(200))
print(st(4))




