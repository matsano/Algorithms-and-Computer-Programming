notac = float(input())
notam = float(input())
notap = float(input())
feriasmi = str(input())
feriasmc = str(input())
liberacaomi = int(input())
liberacaomc = int(input())
valoresh = float(input())
valoresp = float(input())

if not (notac >= 7 and notam >= 7 and notap >= 7):
	print("NAO. As notas da Carla nao foram suficientes.")
else:
	if not (feriasmi == "Sim" and feriasmc == "Sim"):
		print("NAO. O casal nao esta de ferias.")
	else:
		if not (liberacaomi < 11 or liberacaomc < 11):
			print("NAO. Nenhum 13o salario foi liberado a tempo.")
		else:
			if not (valoresh + valoresp <= 10000):
				print("NAO. O valor total e muito alto.")
			else:
				print("SIM!!!")