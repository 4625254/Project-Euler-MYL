count=1
num=2
while count!=10001:
    num+=1
    prime=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            prime=False
    if prime:
        count+=1

print(num)
