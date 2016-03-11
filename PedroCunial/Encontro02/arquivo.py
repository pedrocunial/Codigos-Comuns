texto2 = []

def algo(texto):

	max_p = max((int(x) for x in texto))
	if max_p <= 3:
		return max_p

	i = texto.index(max_p)
	div = max_p // 2
	texto[i] = div
	texto.append(max_p - div)
	rec = 1 + algo(texto)
	return min([max_p, rec])


with open("input.in") as f:
    texto = f.readlines()
    for lines in texto:
    	texto2.append(lines.split())
    print(texto2)

x = algo([1,2,3,4])

with open("output.out", "w") as out:
	out.write(str(x))