def largest_palidrome_product():
    palidrome = 0
    for n in range (800,999):
        for m in range (800, 999):
            p = n * m
            if p // 1000 == p % 10 * 100 + p // 10 % 10 * 10 + p // 100 % 10 and p > palidrome:
                palidrome = p
    return palidrome

print(largest_palidrome_product())


       
        
        
        
        
