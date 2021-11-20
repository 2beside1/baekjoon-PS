l = list(map(int, list(input())))
if 0 not in l or sum(l) % 3 != 0:
    print(-1)
else:
    l.sort(reverse=True)
    print(*l, sep='')
