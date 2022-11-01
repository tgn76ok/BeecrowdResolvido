T=int(input())
for i in range(0, T):
    resl =0
    A, B = input().split(" ")
    if 1 <= len(A) <= 10000 and 1 <= len(B) <= 10000:
        for i in range(0,len(A)):
            if ord(A[i]) <= ord(B[i]):
                resl+= ord(B[i])- ord(A[i])
            else:
                resl += ord(B[i])+26-ord(A[i])
    print(resl)