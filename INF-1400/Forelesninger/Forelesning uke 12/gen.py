
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def next_prime(limit):
    i = 1
    while i < limit:
        if is_prime(i):
            yield i
        i += 1

counter = 0
for i in next_prime(100):
    print(i)