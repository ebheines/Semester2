
def f(x):
    return x*2 + 5

x_verdier = []
y_verdier = []

for i in range(-5, 5):
    x_verdier.append(i)
    y_verdier.append(f(i))

mapping = {}

for x, y in zip(x_verdier, y_verdier):
    mapping[x] = y

print(mapping)