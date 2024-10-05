def my_pow(n: int, p: int):
    out = 1
    while p > 0:
        if p % 2 == 0:
            n *= n
            p /= 2
        else:
            out *= n
            p -= 1
    return out


for k in range(9):
    print(my_pow(2, k))
