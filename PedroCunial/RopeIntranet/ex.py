with open("A-large-practice.in", "r") as fin, open("output.out", "w") as fout:
    T = int(fin.readline().strip())
    for i in range(T):
        N = int(fin.readline().strip())
        lista = []
        while N > 0:
            x = [int(n) for n in fin.readline().strip().split()]
            lista.append(x)
            N -= 1
        soma = 0
        for j in range(len(lista)):
            a = lista[j]
            for k in range(len(lista)):
                b = lista[k]
                if a[0] < b[0]:
                    if a[1] > b[1]:
                        soma += 1
        fout.write("Case #{}: {}\n".format(i+1, soma))



print("done")
