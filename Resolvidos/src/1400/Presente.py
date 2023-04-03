while True:

    N, M = map(int, input().split(" "))

    if N == 0 and M == 0: break
    a = 1
    i = 2
    d = 0
    if (M > 34):
        print("Let me try!")

    else:

        while (a > 0 and a < N + 1):
            if a == M:
                d += 1
                break

            elif a < M:

                if (a + (2 * i - 1) < N + 1):
                    a += 2 * i - 1
                else:
                    a -= 2 * i - 1
                i += 1
            else:
                if (a - (2 * i - 1) > 0):
                    a -= 2 * i - 1
                else:
                    a += 2 * i - 1
                i += 1



        if (d != 0):
            print("Let me try!")

        else:
            print("Don't make fun of me!")

