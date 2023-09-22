c = int(input())
bingo = []
multibingo = []

for i in range(c):
    linha0 = input()
    linha1 = input()
    linha2 = input()
    linha3 = input()
    linha4 = input()
    bingo.append(linha0.split())
    bingo.append(linha1.split())
    bingo.append(linha2.split())
    bingo.append(linha3.split())
    bingo.append(linha4.split())
    multibingo.append(bingo)
    bingo = []

def prt():
    for i in range(c-1):
        print("+----------------+", end = " ")
    print("+----------------+")
    for i in range(c-1):
        print("| B  I  N  G  O  |", end = " ")
    print("| B  I  N  G  O  |")
    for i in range(c-1):
        print("+================+", end = " ")
    print("+================+")
    for i in range(c):
        print("|", end=" ")
        for k in range(5):
            print(multibingo[i][0][k], end=" ")
        if i < c-1:
            print("|", end=" ")
        else:
            print("|")
    for i in range(c):
        print("|", end=" ")
        for k in range(5):
            print(multibingo[i][1][k], end=" ")
        if i < c -1:
            print("|", end=" ")
        else:
            print("|")
    for i in range(c):
        print("|", end=" ")
        for k in range(5):
            print(multibingo[i][2][k], end=" ")
        if i < c -1:
            print("|", end=" ")
        else:
            print("|")
    for i in range(c):
        print("|", end=" ")
        for k in range(5):
            print(multibingo[i][3][k], end=" ")
        if i < c -1:
            print("|", end=" ")
        else:
            print("|")
    for i in range(c):
        print("|", end=" ")
        for k in range(5):
            print(multibingo[i][4][k], end=" ")
        if i < c -1:
            print("|", end=" ")
        else:
            print("|")
    for i in range(c-1):
        print("+----------------+", end=" ")
    print("+----------------+")
prt()

n = int(input())
def bng():
    global c
    for i in range(0, n):
        cont = 0
        bola = input()
        lugar = bola.split("-")
        print(lugar[0] + "-" + lugar[1])
        for l in range(c):
            for m in range(5):
                if lugar[0] == "B":
                    if multibingo[l][m][0] == lugar[1]:
                        multibingo[l][m][0] = "XX"
                        cont += 1
                elif lugar[0] == "I":
                    if multibingo[l][m][1] == lugar[1]:
                        multibingo[l][m][1] = "XX"
                        cont += 1
                elif lugar[0] == "N":
                    if multibingo[l][m][2] == lugar[1]:
                        multibingo[l][m][2] = "XX"
                        cont += 1
                elif lugar[0] == "G":
                    if multibingo[l][m][3] == lugar[1]:
                        multibingo[l][m][3] = "XX"
                        cont += 1
                elif lugar[0] == "O":
                    if multibingo[l][m][4] == lugar[1]:
                        multibingo[l][m][4] = "XX"
                        cont += 1
        if cont > 0:
            prt()
        for a in range(c):
            for b in range(5):
                    if multibingo[a][b][0] == "XX" and multibingo[a][b][1] == "XX" and multibingo[a][b][2] == "XX" and multibingo[a][b][3] == "XX" and multibingo[a][b][4] == "XX":
                        print("BINGO!")
                        return
                    elif multibingo[a][0][b] == "XX" and multibingo[a][1][b] == "XX" and multibingo[a][2][b] == "XX" and multibingo[a][3][b] == "XX" and multibingo[a][4][b] == "XX":
                        print("BINGO!")
                        return
                    elif multibingo[a][0][0] == "XX" and multibingo[a][1][1] == "XX" and multibingo[a][2][2] == "XX" and multibingo[a][3][3] == "XX" and multibingo[a][4][4] == "XX":
                        print("BINGO!")
                        return
                    elif multibingo[a][0][4] == "XX" and multibingo[a][1][3] == "XX" and multibingo[a][2][2] == "XX" and multibingo[a][3][1] == "XX" and multibingo[a][4][0] == "XX":
                        print("BINGO!")
                        return
bng()
