M= int(input())
A= int(input())
B = int(input())

if (40 <= M <= 110) and (1 <= A < M) and (1 <= B < M) and (A != B):
    C = M - A - B

    if C > A and C > B: print(C)
    elif A > C and A > B: print(A)
    else: print(B)