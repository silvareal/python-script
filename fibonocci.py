def fibonocci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for i in fibonocci():
    if i > 10000:
        break
    print(i)