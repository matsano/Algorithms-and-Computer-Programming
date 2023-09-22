l = int(input())
pn = []
h = []
e = []
for i in range(1, l+1, 1):
    p = str(input())
    if p.isalpha():
        pn.append(p)
    else:
        if p.isdigit():
            pn.append(p)
        else:
            if p[0] == "-":
                if p[1:].isdigit():
                    pn.append(p)
                else:
                    e.append(p)
            else:
                if p[0] == "#":
                    if p[1:].isalpha():
                        h.append(p)
                    else:
                        e.append(p)
                else:
                    e.append(p)

n = 0
while(n < len(pn)):
    print(pn[n])
    n = n + 1
if len(h) == 1:
    print("1 hashtag foi removida.")
else:
    if len(h) > 1:
        print(len(h), "hashtags foram removidas.")
if len(e) == 1:
    print("1 emoticon foi removido.")
else:
    if len(e) > 1:
        print(len(e), "emoticons foram removidos.")
