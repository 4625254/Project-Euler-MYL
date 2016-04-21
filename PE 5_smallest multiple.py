def smallest_multiple(y):
    multiple = 1
    factor = 1
    for i in range (2,y+1):
        factor = i
        num = multiple
        for n in range (2,i):
            while factor % n == 0 and num % n == 0:
                factor //= n
                num //= n
        multiple *= factor

    return multiple

print(smallest_multiple(20))
