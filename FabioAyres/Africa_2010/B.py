# -*- coding: utf-8 -*-
#file_in = "B-test.in"
#file_out = "B-test.out"
#file_in = "B-small-practice.in"
#file_out = "B-small-practice.out"
file_in = "B-large-practice.in"
file_out = "B-large-practice.out"

with open(file_in, "r") as fin, open(file_out, "w") as fout:
    N = int(fin.readline().strip())
    for case in range(N):
        fout.write("Case #{0}: {1}\n".format(case + 1, 
                  " ".join(fin.readline().strip().split()[::-1])))

print("done")