texto2 =[]
with open("output2.txt", "w") as out:
	with open("A-large-practice.in") as f:
	    texto = f.readlines()
	    for lines in texto:
	    	texto2.append(lines.split())
	    c = 0
	    for i in range(2,len(texto2),3):
	    	a = [int(n) for n in texto2[i]]
	    	a.sort()
	    	b = [int(n) for n in texto2[i+1]]
	    	b.sort()
	    	b.reverse()
	    	c+=1
	    	k = 0
	    	for j in range(len(a)):
	    		k += a[j]*b[j]
	    	out.write("Case #{0}: {1} \n".format(c,k))