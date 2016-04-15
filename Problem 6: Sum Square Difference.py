def sum_square_diff(n):
    sum_square = (1/6)*n*(n+1)*(2*n+1)
    square_sum = ((1+n)* n / 2)**2

    return square_sum - sum_square

print(sum_square_diff(100))
