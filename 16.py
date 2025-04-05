"""
def f(n):
    if n <= 1:
        return 1/2
    else:
        return (n + 1) * f(n - 1)


result = f(200) / f(198)
print(result)
"""

"""
slovarik = dict()


def f(n):
    if n in slovarik:
        return slovarik[n]
    if n <= 1:
        slovarik[n] = 0.5
    else:
        slovarik[n] = (n + 1) * f(n - 1)


for n in range(1, 100000):
    f(n)
result = f(200) / f(198)
print(result)
"""