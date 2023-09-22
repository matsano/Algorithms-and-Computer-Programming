corteo = float(input())
cortep = float(input())
corteb = float(input())
quantidadeo = 0
quantidadep = 0
quantidadeb = 0
maxnota = 0

while True:
    nota = float(input())
    if nota == -1:
        break
    else:
        if nota >= corteo:
            quantidadeo = quantidadeo + 1
        if nota > maxnota:
            maxnota = nota
        if nota >= cortep and nota < corteo:
            quantidadep = quantidadep + 1
        if nota >= corteb and nota < cortep:
            quantidadeb = quantidadeb + 1

if quantidadeo == 0:
    print("Nenhum participante recebeu medalha de ouro!")
else:
    print("Medalha(s) de ouro:", quantidadeo)

if quantidadep == 0:
    print("Nenhum participante recebeu medalha de prata!")
else:
    print("Medalha(s) de prata:", quantidadep)

if quantidadeb == 0:
    print("Nenhum participante recebeu medalha de bronze!")
else:
    print("Medalha(s) de bronze:", quantidadeb)

print("Maior nota:", maxnota)
