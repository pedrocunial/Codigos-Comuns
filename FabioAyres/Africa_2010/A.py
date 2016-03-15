# -*- coding: utf-8 -*-
#file_in = "A-test.in"
#file_out = "A-test.out"
#file_in = "A-small-practice.in"
#file_out = "A-small-practice.out"
file_in = "A-large-practice.in"
file_out = "A-large-practice.out"

def solve_case(fout, case, C, L):
    n = len(L)
    for i in range(n):
        for j in range(i+1, n):
            if L[i] + L[j] == C:
                fout.write("Case #{0}: {1} {2}\n".format(case+1, i+1, j+1))

with open(file_in, "r") as fin, open(file_out, "w") as fout:
    T = int(fin.readline().strip())
    for case in range(T):
        C = int(fin.readline().strip())
        I = int(fin.readline().strip())
        L = [int(x) for x in fin.readline().strip().split()]
        solve_case(fout, case, C, L)

print("done")