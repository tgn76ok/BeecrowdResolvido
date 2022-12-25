dia,data_inicio=input().split()
data_inicio = int(data_inicio)
hora_inicio,minuto_inicio,segundo_inicio=map(int,input().split(":"))

dia,data_fim=input().split()
data_fim = int(data_fim)
hora_fim,minuto_fim,segundo_fim=map(int,input().split(":"))


if data_inicio>data_fim:
    print("vala docto who, vai viajar no tempo?")
    exit()


s = segundo_fim - segundo_inicio
m = minuto_fim - minuto_inicio
h = hora_fim - hora_inicio
d = data_fim - data_inicio


if hora_fim < hora_inicio:
    h += 24
    d -= 1
if minuto_fim < minuto_inicio:

    m += 60
    h -= 1
if segundo_inicio > segundo_fim:
    s += 60
    m -= 1



print("{0} dia(s)".format(d))
print("{0} hora(s)".format(h))
print("{0} minuto(s)".format(m))
print("{0} segundo(s)".format(s))