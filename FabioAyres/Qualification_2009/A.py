# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
file_in = "A-test.in"
file_out = "A-test.out"
#file_in = "A-small-practice.in"
#file_out = "A-small-practice.out"
#file_in = "A-large-practice.in"
#file_out = "A-large-practice.out"

with open(file_in, "r") as fin, open(file_out, "w") as fout:
    L, D, T = (int(x) for x in fin.readline().strip().split())
    
    words = []
    for i in range(D):
        words.append(fin.readline().strip())
        
    for case in range(T):
        w = fin.readline().strip()
        r = []
        i = 0
        while i < len(w):
            item = []
            if w[i] == '(':
                i += 1
                while w[i] != ')':
                    item.append(w[i])
                    i += 1
                r.append(item)
            else:
                r.append([w[i]])
            i += 1

print("done")