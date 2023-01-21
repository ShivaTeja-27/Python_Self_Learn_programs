num = 10

m = (2 * num) - 2

for i in range(0, num):
    for j in range(0, m):
        print(end=" ")
    m = m - 1

    for j in range(0, i + 1):

        print("#", end=" ")
    print(" ")
