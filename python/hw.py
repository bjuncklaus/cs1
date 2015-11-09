l = [0]


def hs(n):
    print(n)
    l[0] += 1
    if (n != 1):
        if (n % 2 == 0):
            n //= 2
        else:
            n = 3 * n + 1
        hs(n)
    else:
        print(l[0])
        return None
