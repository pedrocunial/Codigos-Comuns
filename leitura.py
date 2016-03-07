texto2 = []

with open("input.in") as f:
    texto = f.readlines()
    for lines in texto:
    	texto2.append(lines.split())
    print(texto2)

with open("output.out", "w") as out: