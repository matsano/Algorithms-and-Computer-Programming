n = input()
n = str(n.zfill(3))
ns = input()
ns = ns.split(" ")
for i in range(len(ns)):
    ns[i] = str(ns[i].zfill(3))

def buscaBinaria(ns, n):
    global meio
    inicio = 0
    fim = len(ns)-1
    while inicio <= fim:
        meio = (inicio + fim)//2
        for i in range(len(ns)):
            if ns[i] == "   ":
                print("      ", end="")
            elif i == meio:
                print("+=====",end="")
            else:
                print("+-----",end="")
        print("+")
        for i in range(len(ns)):
            if ns[i] == "   ":
                print("      ", end="")
            elif i == meio:
                print("|" + "|" + ns[i] + "|", end="")
            else:
                print("|" + " " + ns[i] + " ", end="")
        print("|")
        for i in range(len(ns)):
            if ns[i] == "   ":
                print("      ", end="")
            elif i == meio:
                print("+=====",end="")
            else:
                print("+-----",end="")
        print("+")
        if ns[meio] == n:
            print("O elemento estah na posicao", meio)
            return
        elif ns[meio] > n:
            i = 0
            while i < len(ns) - meio:
                del ns[meio]
            i = 0
            fim = meio - 1
        else:
            j = 0
            while j <= meio:
                ns[j] = "   "
                j+=1
            j=0
            inicio = meio + 1
    return -1

print("Elemento procurado:", n)

for i in range(len(ns)-1):
    print("+-----", end="")
print("+-----+")

for i in range(len(ns)):
    print("| " + ns[i] + " ", end="")
print("|")

for i in range(len(ns)-1):
    print("+-----", end="")
print("+-----+")
cont = 0
for i in range(len(ns)-1):
    if ns[i] > ns[i+1]:
        cont += 1
if cont != 0:
    print("Vetor nao estah ordenado")
else:
    if (buscaBinaria(ns, n) == -1):
        print("O elemento nao foi encontrado")
