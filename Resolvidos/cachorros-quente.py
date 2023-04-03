#(1 ≤ H, P ≤ 1000) h =total de cachorros quentes p=total de participantes na competição.
h, p = map(int, input().split(" "))
if (1 <= h) and (p <= 1000):
    print("{:.2f}".format(h/p))
