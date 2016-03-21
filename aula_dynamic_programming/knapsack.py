# -*- coding: utf-8 -*-

memo = {}

def best(W, P):
    if W in memo:
        return memo[W][0]
    m = 0
    w_best = -1
    for w,v in P:
        w_left = W - w
        if w_left >= 0:
            m_test = v + best(w_left, P)
            if m < m_test:
                m = m_test
                w_best = w
    # Note: it may be the case that m == 0, w_best == -1, if no W - w > 0.
    memo[W] = (m, w_best)
    print(memo)
    return m

back = []

def backtrack(W):
    if W in memo:
        this_w = memo[W][1]
        if this_w != -1:
            back.append(this_w)
            backtrack(W - this_w)
    

W = 10
P = [(5,5), (3,2), (1,0), (10,6), (8,5)]

print(best(W,P))   
backtrack(W)
print(back) 