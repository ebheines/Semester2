import time

def hei():
    print("Heisann hoppsann")

def hallo():
    print("Hallo på do din gamle sko")

def kjip():
    s = 0
    for i in range(1000000):
        s += 1
    print("hehe, du ble molesta av en tannfe")

def hva_skjer(func):
    print("Calling function", func)
    start = time.time()
    func()
    end = time.time() - start
    print("Function call took", end, "seconds")
    print("\n")

def time_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time() - start
        return end
    return wrapper


timed_kjip = time_decorator(kjip)

runtime = timed_kjip()
print("Runtime of kjip (sec):",runtime)