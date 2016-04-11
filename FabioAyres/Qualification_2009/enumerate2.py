import itertools

a = [[1, 2, 3], ["a", "b"]]

for b in itertools.product(*a):
    print(b)

for b in itertools.product(a[0], a[1]):
    print(b)
