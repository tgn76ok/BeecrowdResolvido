N = int(input())
s = b = a = s1 = b1 = a1 = 0

for i in range(N):
    nome = str(input())
    S,B,A = map(int, input().split(' '))

    s += S
    b += B
    a += A

    S1,B1,A1 = map(int, input().split(' '))

    s1 += S1
    b1 += B1
    a1 += A1
print('Pontos de Saque: {:.2f} %.'.format(s1 * 100 / s))
print('Pontos de Bloqueio: {:.2f} %.'.format(b1 * 100 / b))
print('Pontos de Ataque: {:.2f} %.'.format(a1 * 100 / a))