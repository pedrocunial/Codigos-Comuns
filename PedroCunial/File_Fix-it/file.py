
"""
Não consegui fazer este exercício, mas deixei algumas das minhas tentativas como comentario
"""

with open("input.in", "r") as fin, open("output.out", "w") as fout:
    T = int(fin.readline().strip())
    for i in range(T):
        N, M = ([int(x) for x in fin.readline().strip().split()])
        mkdir_counter = 0
        diretorios = ['']
        for c in range(N):
            diretorios.append([d for d in fin.readline().strip().split('/')])
        print diretorios
        for c in range(M):
            di = [d for d in fin.readline().strip().split('/')]
            print(di)
            for b in range(len(di)):
                if di[-b-1] not in diretorios:
                    diretorios.append(di)
                    mkdir_counter+=1



                    # # indices = [i for i, x in enumerate(diretorios) if x == di[g]]
                    # # for p in range(len(indices)):
                    # #     if g != diretorios[indices[p]].index():
                    # for pasta in diretorios:
                    #     if di[g] in pasta:
                    #         new_pasta = [p for p in pasta]
                    #         while len(new_pasta) > 0:
                    #             particle = new_pasta.pop()
                    #             if particle == di[g]:
                    #                 if len(new_pasta) != g+1:
                    #                     mkdir_counter+=1
                    #                     diretorios.append(di[g])
                    #                     break


        print "counter"
        print mkdir_counter

        print "diretorios: "
        print diretorios
