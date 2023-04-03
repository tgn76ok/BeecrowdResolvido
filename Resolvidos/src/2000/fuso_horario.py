HSaida, tmp_viagem, FusoH = map(int, input().split(" "))
Hchegada = 0
if (0 <= HSaida <= 23) and (1 <= tmp_viagem <= 12) and (-5 <= FusoH <= 5):
    if HSaida == 0:
        HSaida = 24
    Hchegada = HSaida + tmp_viagem + FusoH
    if Hchegada >= 24:
        Hchegada -= 24

print(Hchegada)
