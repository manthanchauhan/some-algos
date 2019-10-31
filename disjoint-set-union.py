t = int(input())

while t:
    t -= 1
    n, q = input().split()
    n, q = int(n), int(q)

    dsu = [None] * (n + 1)
    for i in range(1, n + 1):
        dsu[i] = i

    while n - 1:
        n -= 1
        u, v = input().split()


    def root(i):
        if dsu[i] == i:
            return i, False
        else:
            comp = False

            if dsu[i] < 0:
                comp = True

            r, comp_ = root(abs(dsu[i]))
            return r, (comp_ and not comp) or (comp and not comp_)


    queries = []
    while q:
        q -= 1
        u, v, x = input().split()
        u, v, x = int(u), int(v), int(x)
        queries.append((u, v, x))

        ru, cu = root(u)
        rv, cv = root(v)

        if x:
            if (cu and not cv) or (cv and not cu):
                dsu[ru] = rv
            else:
                dsu[ru] = -rv
        else:
            if (cu and not cv) or (cv and not cu):
                dsu[ru] = -rv
            else:
                dsu[ru] = rv

    check = [None] * len(dsu)
    exp = 0
    for i in dsu[1:]:
        if i == dsu[i]:
            exp += 1
            check[i] = 0
        else:
            r, comp = root(i)
            check[i] = comp

    ans = True
    for u, v, x in queries:
        if check[u] ^ check[v] != x:
            ans = False
            break

    if not ans:
        print(0)
        continue

    print(2 ** exp)




