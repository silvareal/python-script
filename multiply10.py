for i in range(1,11):
    print('{:<5}|'.format(i),end="")

    for j in range(1,11):
        print('{:<4}|'.format(i * j),end="")
