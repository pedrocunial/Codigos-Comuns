texto2 = []
amigos = 0
with open("A-large-practice.in") as f:
    texto = f.readlines()
    for lines in texto:
    	texto2.append(lines.split())

print(texto2, "bla")		
arquivo = open("output.out", "w")

for i in range(1,int(texto2[0][0]) + 1):
#	for j in range(0, len(texto2[i])):
	numero = texto[i].split(" ")
	jonas = numero[1].strip()
	smax = int(numero[0])
	shy = [int(x) for x in jonas]
	soma = shy[0]
	amigos = 0 

	for level in range(1, smax + 1):
		more_friends = (level - soma) if soma < level else 0
		amigos += more_friends
		soma += shy[level] + more_friends

	arquivo.write("Case #")
	arquivo.write(str(i))
	arquivo.write(": ")
	arquivo.write(str(amigos))
	arquivo.write("\n")

# 	arquivo.write(numero[0])
# 	arquivo.write(" ")
# 	arquivo.write(numero[1])
# 	arquivo.write("\n")

arquivo.close()
