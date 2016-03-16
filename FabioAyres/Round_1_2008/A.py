# -*- coding: utf-8 -*-
#file_in = "A-test.in"
#file_out = "A-test.out"
#file_in = "A-small-practice.in"
#file_out = "A-small-practice.out"
file_in = "A-large-practice.in"
file_out = "A-large-practice.out"

with open(file_in, "r") as fin, open(file_out, "w") as fout:
    T = int(fin.readline().strip())
    for case in range(T):
        n = int(fin.readline().strip())
        x = [int(i) for i in fin.readline().strip().split()]
        x.sort()
        y = [int(i) for i in fin.readline().strip().split()]
        y.sort(reverse=True)
        s = sum([i*j for i,j in zip(x, y)])
        fout.write("Case #{0}: {1}\n".format(case + 1, s))

print("done")