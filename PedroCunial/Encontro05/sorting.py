with open("A-large-practice.in", "r") as f, open("output.out", "w") as out:
    T = int(f.readline().strip())
    for caso in range(T):
        n = int(f.readline().strip()) # linha indice
        print(n)
        v1 = [int(x) for x in f.readline().strip().split()] # primeiro vetor
        v1.sort()
        v2 = [int(x) for x in f.readline().strip().split()] # segundo vetor
        v2.sort(reverse=True)
        soma = sum([x*y for x, y in zip(v1, v2)])
        out.write("Case #{}: {}\n".format(caso + 1, soma))
