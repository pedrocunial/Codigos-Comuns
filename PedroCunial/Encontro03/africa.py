texto2 = []

with open("B-large-practice.in") as f:
    texto = f.readlines()
    for lines in texto:
    	texto2.append(lines.split())
    print(texto2)

with open("output.out", "w") as out:
	c = 1
	for i in range(1, len(texto2)):
		bla = []
		for j in range(len(texto2[i])):
			bla.append(texto2[i][-(j + 1)])

		out.write("Case #{}: ".format(c))
		for word in bla:
			out.write(word)
			out.write(" ")
		out.write("\n")
		del bla[:]
		c+=1