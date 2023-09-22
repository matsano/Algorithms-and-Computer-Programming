lista_palavras = ["perfeitamente", "liberdade", "enfermidade",
                  "significado", "outono", "chuva", "ilha",
                  "infinito", "solidariedade", "ameixa",
                  "felicidade", "arte", "paternidade",
                  "criatividade", "virtude", "guerra",
                  "democracia", "teatro", "saudade", "adeus",
                  "paz", "honestidade", "horizonte", "sabedoria",
                  "sossego", "maternidade", "esperteza",
                  "primavera", "coragem", "igualdade",
                  "navio", "montanha", "queijo",
                  "gentileza", "tempestade", "joalheria",
                  "paralelogramo", "melancolia", "trem",
                  "inverno", "amizade", "atriz",
                  "computador", "borboleta", "aeroporto",
                  "nascimento", "uva", "oceano", "orquestra",
                  "melancia"]

cenas_forca = [
"""+++++
|   |
|
|
|
+_______""",

"""+++++
|   |
|   O
|
|
+_______""",

"""+++++
|   |
|   O
|   |
|
+_______""",
"""+++++
|   |
|   O
|  /|
|
+_______""",

"""+++++
|   |
|   O
|  /|\\
|
+_______""",

"""+++++
|   |
|   O
|  /|\\
|  /
+_______""",

"""+++++
|   |
|   O
|  /|\\
|  / \\
+_______"""

]

cf = 0
ti = []
lc = []
lt = []
trocas = 0
t = 0
x = int(input("Escolha um numero entre 0 e 49: "))
if x < 0 or x > 49:
    print("Numero invalido.")
else:
    print("")
    f = len(lista_palavras[x])-1
    print(cenas_forca[0])
    palavra = list(lista_palavras[x])
    n = len(palavra)
    resposta = [" _ " for i in range(n-1)]
    resposta.append(" _")
    print("Palavra:", end="")
    for i in range(0, len(palavra)-1):
        print(" _ ", end="")
    print(" _")
    print("Proxima letra:", end=" ")

    while len(ti) <= 5:
        l = input()
        if l in lt:
            print("Voce jah escolheu esta letra.")
        print("")
        if l in palavra and l not in lt:
            print(cenas_forca[cf])
            for j in range(0, len(resposta)-1):
                if l == palavra[j]:
                    del resposta[j]
                    resposta.insert(j," " + l + " ")
                    trocas+=1
            if l == palavra[f]:
                del resposta[f]
                resposta.insert(f," " + l)
                trocas+=1
            if l not in lc:
                lc.append(l)
            print("Palavra:", end="")
            for i in range(0, len(palavra)):
                print(resposta[i], end="")
            print("")
        elif l not in palavra and l not in lt:
            cf = cf + 1
            print(cenas_forca[cf])
            print("Palavra:", end="")
            for i in range(0, len(palavra)):
                print(resposta[i], end="")
            print("")
        if l in lt:
            print(cenas_forca[cf])
            print("Palavra:", end="")
            for i in range(0, len(palavra)):
                print(resposta[i], end="")
            print("")
        if l not in palavra:
            t = 1
            if l not in ti:
                ti.append(l)
        if t == 1:
            print("Tentativa(s) incorreta(s):", end="")
            for m in range(0,len(ti)):
                print("",ti[m], end="")
            print("")
        if len(palavra) > len(lc) and trocas != len(lista_palavras[x]) and len(ti) != 6:
            print("Proxima letra:", end=" ")
        lt.append(l)
        if len(ti) == 6:
            print("Palavra oculta:", lista_palavras[x])
            break
        if trocas == len(lista_palavras[x]):
            print("Palavra encontrada!")
            break

input()
