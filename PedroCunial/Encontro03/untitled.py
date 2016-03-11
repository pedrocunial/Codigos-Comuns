texto2 = []

with open("A-large-practice.in") as f:
    texto = f.readlines()
    for lines in texto:
    	texto2.append(lines.split())
    print(texto2)

with open("output.out", "w") as out:
	c = 1
	for i in range(1, len(texto2) , 3):
		otimo = 0
		produtos = []
		for j in range(len(texto2[i+2])):
			for k in range(len(texto2[i+2])):
				if k == j:
					pass
				else:
					preco = (int(texto2[i+2][j]) + int(texto2[i+2][k]))
					if (preco > otimo) and  (preco <= int(texto2[i][0])):
						produtos = [j+1, k+1]
						otimo = preco

		out.write("Case #")
		out.write(str(c))
		out.write(": ")
		out.write(str(produtos[0]))
		out.write(" ")
		out.write(str(produtos[1]))
		out.write("\n")
		c+=1