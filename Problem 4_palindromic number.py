def largest_palidrome_product():
    n = 800
    m = 800
    palidrome = 0
    while n < 999:
        while m < 999:
            p = n * m
            if p // 1000 == p % 10 * 100 + p // 10 % 10 * 10 + p // 100 % 10 and p > palidrome:
                palidrome = p
            m += 1
        n += 1
        m = 800
    return palidrome

print(largest_palidrome_product())


       
        
        
        
        
