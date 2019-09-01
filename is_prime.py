
def is_prime(num):
    p = [i for i in range(2, num) if num % i == 0]
    print(len(p))
    if len(p) == 0 and len(p) >= 2:
        print('not a prime no')
    else:
        print('is prime no')

pp = is_prime(13)
print(pp)
