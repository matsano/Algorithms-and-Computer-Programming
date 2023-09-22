n = int(input())
times = {}
pontuacao = {}
vitorias = {}
saldo = {}
gols = {}
campeao = 0
p = -100
v = -100
sg = -100
gp = -100

for i in range(0, n*(n-1)):
    partida = input()
    sobre_partida = partida.replace("x"," ")
    sobre_partida = sobre_partida.split()
    
    if not sobre_partida[0] in times:
        times[sobre_partida[0]] = 0
        pontuacao[sobre_partida[0]] = 0
        vitorias[sobre_partida[0]] = 0
        saldo[sobre_partida[0]] = 0
        gols[sobre_partida[0]] = 0

    if not sobre_partida[2] in times:
        times[sobre_partida[2]] = 0
        pontuacao[sobre_partida[2]] = 0
        vitorias[sobre_partida[2]] = 0
        saldo[sobre_partida[2]] = 0
        gols[sobre_partida[2]] = 0

    if sobre_partida[1] > sobre_partida[3]:
        pontuacao[sobre_partida[0]] = int(pontuacao[sobre_partida[0]]) + 3
        vitorias[sobre_partida[0]] = int(vitorias[sobre_partida[0]]) + 1
    elif sobre_partida[1] == sobre_partida[3]:
        pontuacao[sobre_partida[0]] = int(pontuacao[sobre_partida[0]]) + 1
    if sobre_partida[3] > sobre_partida[1]:
        pontuacao[sobre_partida[2]] = int(pontuacao[sobre_partida[2]]) + 3
        vitorias[sobre_partida[2]] = int(vitorias[sobre_partida[2]]) + 1
    elif sobre_partida[3] == sobre_partida[1]:
        pontuacao[sobre_partida[2]] = int(pontuacao[sobre_partida[2]]) + 1

    gols[sobre_partida[0]] = int(gols[sobre_partida[0]]) + int(sobre_partida[1])
    gols[sobre_partida[2]] = int(gols[sobre_partida[2]]) + int(sobre_partida[3])

    saldo[sobre_partida[0]] = int(saldo[sobre_partida[0]]) + int(sobre_partida[1]) - int(sobre_partida[3])
    saldo[sobre_partida[2]] = int(saldo[sobre_partida[2]]) + int(sobre_partida[3]) - int(sobre_partida[1])

for t in sorted(times):
    print(t, pontuacao[t], vitorias[t], saldo[t], gols[t])
    if int(pontuacao[t]) > p:
        p = int(pontuacao[t])
        campeao = t
        v = int(vitorias[t])
        sg = int(saldo[t])
        gp = int(gols[t])
    elif int(pontuacao[t]) == p:
        if int(vitorias[t]) > v:
            v = int(vitorias[t])
            campeao = t
            sg = int(saldo[t])
            gp = int(gols[t])
        elif int(vitorias[t]) == v:
            if int(saldo[t]) > sg:
                sg = int(saldo[t])
                campeao = t
                gp = int(gols[t])
            elif int(saldo[t]) == sg:
                if int(gols[t]) > gp:
                    gp = int(gols[t])
                    campeao = t

print("Vencedor:", campeao)
