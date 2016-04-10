import itertools as it

texto2 =[]
with open("output2.txt", "w") as out:
	with open("teste.txt") as f:
		L,D,T = (int(x) for x in f.readline().strip().split())

		palavras = set()
		for d in range(D):
			palavras.add(f.readline().strip())

		for case in range(T):

			w = f.readline().strip()

			r = []
			i = 0

			while i < len(w):
				item = []
				if w[i] == '(':
					i+=1
					while w[i] != ')':
						item.append(w[i])
						i+=1
					i+=1
				else:
					item.append(w[i])
					i+=1

				r.append(item)
			print(r)

			count = 0
			for item in it.product(*r):
				s = ("".join(item))
				if s in palavras:
					count+=1

			out.write("Case #{0}: {1} \n".format(case+1,count))