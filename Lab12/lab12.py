n = input()
n = n.split(" ")

for k in range(len(n)):
    n[k] = str(n[k].zfill(2))

def bubbleSort(n):
    for i in range(len(n)-1,0,-1):
        for j in range(i):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
                printar(n)
def printar(n):
    for k in range(len(n) + 1):
        print(".", end = "")
    print(".")
    a = 0
    b = 0
    grafico = []
    for k in range(len(n)):
        if int(n[k]) > a:
            a = int(n[k])
            b = k
    for k in range(len(n)):
        c = int(n[k])*"|" + (a - int(n[k]))*" "
        c = list(c)
        grafico.append(c)
    for k in range(a-1,-1,-1):
        print(".", end="")
        for t in range(len(n)):
            print(grafico[t][k], end="")
        print(".")
    for k in range(len(n) + 1):
        print(".", end = "")
    print(".")
printar(n)
bubbleSort(n)
