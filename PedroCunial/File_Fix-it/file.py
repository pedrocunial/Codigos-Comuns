 # -*- coding: utf-8 -*-

"""
Não consegui fazer este exercício, mas deixei algumas das minhas
tentativas como comentario
"""
#
# def le_chaves(dicionario, chave):
#     if chave in dicionario:
#         return dicionario[chave]
#     dicionario[chave] = {}
#     return dicionario


with open("input.in", "r") as fin, open("output.out", "w") as fout:
    T = int(fin.readline().strip())
    for i in range(T):
        N, M = ([int(x) for x in fin.readline().strip().split()])
        mkdir_counter = 0
        diretorios = {}
        print N, M
        for c in range(N):
            chaves = [d for d in fin.readline().strip().split('/')]
            with open("gambiarra.gbr", "w") as gambiarra:
                gambiarra.write("diretorios")
                for i in range(1, len(chaves)):
                    gambiarra.write("['")
                    gambiarra.write(chaves[i])
                    gambiarra.write("']")
                    # if chaves[i] in dicionario
                gambiarra.write("={}")
                with open("gambiarra.gbr", "r") as sujeira:
                    string = (sujeira.readline())
                    eval(string)
                    print diretorios

        print "counter:"
        print mkdir_counter

        print "diretorios: "
        print diretorios
