def factor(n):

    if n <= 1:
        f = 1
    else:
        f = factor(n-1) * n
    print(f)

factor(5)
