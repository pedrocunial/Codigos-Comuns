texto2 = []

with open("C-large-practice.in") as f:
	texto = f.readlines()
	for lines in texto:
		texto2.append(lines.rstrip("\n"))
	print(texto2)

with open("output.out", "w") as out:
	alfa = {"a": "2", "b": "22", "c": "222",
	 		"d": "3", "e": "33", "f": "333",
	 		"g": "4", "h": "44", "i": "444",
	 		"j": "5", "k": "55", "l": "555",
	 		"m": "6", "n": "66", "o": "666",
	 		"p": "7", "q": "77", "r": "777", "s": "7777",
	 		"t": "8", "u": "88", "v": "888",
	 		"w": "9", "x": "99", "y": "999", "z": "9999",
			" ": "0"}


			# for testing
	alfafa = {0: [' '], 2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'],
			  4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'],
			  6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'],
			  8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}


	print(type(alfa))
	k = 1

	for j in range(1,len(texto2)):
		l_pas = "a"
		out.write("Case #{}: ".format(k))

		for c in texto2[j]:
			l = alfa[c]

			if l[0] == l_pas[0]:
				out.write(" ")
			
			out.write(l)
			l_pas = l
		out.write("\n")
		k += 1