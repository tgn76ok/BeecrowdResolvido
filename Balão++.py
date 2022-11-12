Raio, Gas = input().split(" ")

r = int(Raio)
l = int(Gas)
v = (12.566 * (r ** 3)) / 3
q = int(l // v)
print(q)