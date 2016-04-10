import itertools as it

with open("output2.txt", "w") as out:
	with open("teste.txt") as f:
		l = f.readline()
		for i in range(int(l)):
			K,C,S = (int(x) for x in f.readline().strip().split())
			casa = 0
			lista = []	
			for n in range(1,K):
				for c in range(1,C):
					casa += (K**(c-1))*(n)
			if n == 1:
				casa += 1
				lista.append(casa)
				print(lista)
			h = ''
			for e in lista:
				h += str(e)
				h += ' '
			out.write("Case #{0}: {1} \n".format(i+1,e))