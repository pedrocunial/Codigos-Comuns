# -*- coding: utf-8 -*-
#file_in = "C-test.in"
#file_out = "C-test.out"
#file_in = "C-small-practice.in"
#file_out = "C-small-practice.out"
file_in = "C-large-practice.in"
file_out = "C-large-practice.out"

def translate(c):
    if c in "abc":
        return 2, ("abc".find(c) + 1)
    elif c in "def":
        return 3, ("def".find(c) + 1)
    elif c in "ghi":
        return 4, ("ghi".find(c) + 1)
    elif c in "jkl":
        return 5, ("jkl".find(c) + 1)
    elif c in "mno":
        return 6, ("mno".find(c) + 1)
    elif c in "pqrs":
        return 7, ("pqrs".find(c) + 1)
    elif c in "tuv":
        return 8, ("tuv".find(c) + 1)
    elif c in "wxyz":
        return 9, ("wxyz".find(c) + 1)
    elif c == ' ':
        return 0, 1
    else:
        return 0, 0

def solve(case, fout, msg):
    s = ""
    previous_key = -1
    for c in msg:
        key, rep = translate(c)
        if key == previous_key:
            s += " "
        s += str(key)*rep
        previous_key = key
    fout.write("Case #{0}: {1}\n".format(case+1, s))
            

with open(file_in, "r") as fin, open(file_out, "w") as fout:
    N = int(fin.readline().strip())
    for case in range(N):
        msg = fin.readline()
        solve(case, fout, msg)

print("done")