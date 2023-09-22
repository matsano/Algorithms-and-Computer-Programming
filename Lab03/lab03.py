figura = str(input())
caractere = str(input())

if figura == "Q" or figura == "L" or figura == "C":
    lado = int(input())
    largura = 3
    altura = 3
if figura == "R" or figura == "P":
    largura = int(input())
    altura = int(input())
    lado = 3
if figura != "Q" and figura != "L" and figura != "C" and figura != "R" and figura != "P":
    print("Objeto incorreto.")
else:
    if lado < 3 or largura < 3 or altura < 3:
        print("Dimensao incorreta.")
    else:
        if figura == "Q":
            print(caractere*lado)
            for i in range (0,lado-2,1):
                print(caractere + (lado-2)*' ' + caractere)
            print(caractere*lado)
        if figura == "R":
            print(caractere*largura)
            for i in range (0,altura-2,1):
                print(caractere + (largura-2)*' ' + caractere)
            print(caractere*largura)

        if figura == "P":
            print(caractere*largura)
            for i in range (0,altura-2,1):
                print((i + 1)*' ' + caractere + (largura-2)*' ' + caractere)
            print((altura-1)*' ' + caractere*largura)

        if figura == "C":
            print(lado*' ' + caractere*lado)
            for i in range (0,lado-2,1):
                print(lado*' ' + caractere + (lado-2)*' ' + caractere)
            print(lado*3*caractere)
            for i in range (0,lado-2,1):
                print(3*(caractere + (lado-2)*' ' + caractere))
            print(lado*3*caractere)
            for i in range (0,lado-2,1):
                print(lado*' ' + caractere + (lado-2)*' ' + caractere)
            print(lado*' ' + caractere*lado)

        if figura == "L":
            print((lado-1)*' ' + caractere)
            for i in range (lado-1,0,-1):
                print((i-1)*' ' + caractere + (2*(lado-i)-1)*' ' + caractere)
            for i in range (0,lado-2,1):
                print((i + 1)*' ' + caractere + (lado*2-2*(i+1)-3)*' ' + caractere)
            print((lado-1)*' ' + caractere)
