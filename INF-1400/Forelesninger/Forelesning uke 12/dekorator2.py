import time

def timer(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        runtime = time.time() - start
        return runtime, result
    return wrapper

@timer
def add(a, b):
    return a + b

@timer
def multiply(a, b):
    return a * b


tid, verdi = add(12, 12)

print("Time used: ", tid)
print("Value returned: ", verdi)