A, B, C = 300, 60, 10

T = int(input())
if T % 10 != 0:
    print('-1')
else:
    a = T//A
    T = T % A
    b = T//B
    T = T % B
    c = T//C
    print(a, b, c)
