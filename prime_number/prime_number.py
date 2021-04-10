def is_prime(n):
    avval = True
    for i in range(2, n):
        if n % i == 0:
            avval = False
    return avval


count = 0
for i in range(1, 1001):
    if is_prime(i):
        count = count+1
        print(i)

print()
print("we had ", count, "prime number")
