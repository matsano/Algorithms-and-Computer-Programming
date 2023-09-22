linha0 = input()
linha1 = input()
linha2 = input()
linha3 = input()
linha4 = input()

print("+----------------+")
print("| B  I  N  G  O  |")
print("+================+")
print("|", linha0, "|")
print("|", linha1, "|")
print("|", linha2, "|")
print("|", linha3, "|")
print("|", linha4, "|")
print("+----------------+")

n = int(input())
linha0 = linha0.split(" ")
linha1 = linha1.split(" ")
linha2 = linha2.split(" ")
linha3 = linha3.split(" ")
linha4 = linha4.split(" ")
bingo = [linha0, linha1, linha2, linha3, linha4]

for i in range(0, n):
    lugar = input()
    lugar = lugar.split("-")
    if lugar[1] in linha0 or lugar[1] in linha1 or lugar[1] in linha2 or lugar[1] in linha3 or lugar[1] in linha4:
        for j in range(5):
            for k in range(5):
                if bingo[j][k] == lugar[1]:
                    bingo[j][k] = "XX"
        print(lugar[0] + "-" + lugar[1])
        print("+----------------+")
        print("| B  I  N  G  O  |")
        print("+================+")
        print("|", end=" ")
        for j in range(5):
            print(linha0[j],end=" ")
        print("|")
        print("|", end=" ")
        for k in range(5):
            print(linha1[k],end=" ")
        print("|")
        print("|", end=" ")
        for l in range(5):
            print(linha2[l],end=" ")
        print("|")
        print("|", end=" ")
        for m in range(5):
            print(linha3[m],end=" ")
        print("|")
        print("|", end=" ")
        for n in range(5):
            print(linha4[n],end=" ")
        print("|")
        print("+----------------+")
    else:
        print(lugar[0] + "-" + lugar[1])

    if linha0[0] == linha1[0] == linha2[0] == linha3[0] == linha4[0] == "XX":
        print("BINGO!")
        break
    elif linha0[1] == linha1[1] == linha2[1] == linha3[1] == linha4[1] == "XX":
        print("BINGO!")
        break
    elif linha0[2] == linha1[2] == linha2[2] == linha3[2] == linha4[2] == "XX":
        print("BINGO!")
        break
    elif linha0[3] == linha1[3] == linha2[3] == linha3[3] == linha4[3] == "XX":
        print("BINGO!")
        break
    elif linha0[4] == linha1[4] == linha2[4] == linha3[4] == linha4[4] == "XX":
        print("BINGO!")
        break
    elif linha0[0] == linha1[1] == linha2[2] == linha3[3] == linha4[4] == "XX":
        print("BINGO!")
        break
    elif linha0[0] == linha0[1] == linha0[2] == linha0[3] == linha0[4] == "XX":
        print("BINGO!")
        break
    elif linha1[0] == linha1[1] == linha1[2] == linha1[3] == linha1[4] == "XX":
        print("BINGO!")
        break
    elif linha2[0] == linha2[1] == linha2[2] == linha2[3] == linha2[4] == "XX":
        print("BINGO!")
        break
    elif linha3[0] == linha3[1] == linha3[2] == linha3[3] == linha3[4] == "XX":
        print("BINGO!")
        break
    elif linha4[0] == linha4[1] == linha4[2] == linha4[3] == linha4[4] == "XX":
        print("BINGO!")
        break
    elif linha0[0] == linha1[1] == linha2[2] == linha3[3] == linha4[4] == "XX":
        print("BINGO!")
        break
    elif linha0[4] == linha1[3] == linha2[2] == linha3[1] == linha4[0] == "XX":
        print("BINGO!")
        break
