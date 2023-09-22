ac = []
ac = [float(x) for x in input().split()]
sac = 0
for i in range (0, len(ac)):
    sac = sac + ac[i]
mac = sac / len(ac)
print("Media das atividades conceituais:", format(mac, ".1f"))

lab = ()
def tupla_float_int(x) :
    x = x[1:-1]
    x = x.split(",")
    f = float(x[0])
    i = int(x[1])
    return (f,i)
slab = 0
plab = 0
lab = [tupla_float_int(x) for x in input().split()]
for j in range (0, len(lab)):
    slab = slab + float(format(lab[j][0], ".1f"))*int(lab[j][1])
    plab = plab + lab[j][1]
mlab = slab / plab
print("Media das tarefas de laboratorio:", format(mlab, ".1f"))

p = []
p = [float(x) for x in input().split()]
mp = (p[0]*2 + p[1]*3)/5
print("Media das provas:", format(mp, ".1f"))

f = int(input())
if f >= 75:
    if mp >= 5 and mlab >= 5:
        md = 0.6*mp + 0.3*mlab + 0.1*mac
        mf = max(5, md)
        print("Aprovado(a) por nota e frequencia.")
        print("Media final:", format(mf, ".1f"))
    elif mp < 2.5 or mlab < 2.5:
        mf = min(mp, mlab)
        print("Reprovado(a) por nota.")
        print("Media final:", format(mf, ".1f"))
    else:
        e = float(input())
        mf = (min(mp, mlab) + e)/2
        print("Nota no exame:", e)
        if mf >= 5.0:
            print("Aprovado(a) por nota e frequencia.")
            print("Media final:", format(mf, ".1f"))
        else:
            print("Reprovado(a) por nota.")
            print("Media final:", format(mf, ".1f"))
else:
    print("Reprovado(a) por frequencia.")
    print("Media final:", min(mp, mlab))

