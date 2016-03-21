w = 10
# notação (w, v) -- Peso, valor
p = [(5,5), (3,2), (1,0), (10,6), (8,5)]

memo = {}
def top_down(w):
    if w <= 0:
        return 0
    if w in memo:
        return memo[w]
    m = 0
    for w_item, v_item in p:
        w_left = w - w_item
        if w_left >= 0:
            this_value = v_item + top_down(w_left)
            if m < this_value:
                m = this_value
    memo[w] = m
    return m

def bottom_up(w):
    escolhas = [0] * (w+1)
    f = [-1] * (w+1)
    for w_bag in range(w+1):
        m = -1
        e = -1
        for w_item, v_item in p:
            w_left = w - w_item
            if w_left >= 0:
                this_value = v_item + f[w_left]
                if m < this_value:
                    e = w_item
                    m = this_value
        f[w_bag] = m
        escolhas[w_bag] = e
    print(f[w])
    print(escolhas[w])
    return [f, escolhas]
    # return f

# função do fabio
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

# primeira parte da solução do ayres
def bottom_ayres(w):
    # Solve each case.
    F = [(0, -1)]
    for w_total in range(1, w + 1):
        # Solve this case.
        best_item = (0, -1)
        best_bag_value = -1
        for w, v in p:
            w_left = w_total - w
            if w_left >= 0:
                this_bag_value = v + F[w_left][1]
                if this_bag_value > best_bag_value:
                    best_bag_value = this_bag_value
                    best_item = (w, v)
        F.append(best_item)
    return F

# parte dois da solução do ayres
def backtrack(F, w):
    # Backtrack.
    bag = []
    c = 0
    while w > 0:
        item = F[w]
        bag.append(item[0])
        w -= item[0]
    return bag


print(bottom_up(w))
# print(backtrack(bottom_ayres(w), w))
print("O melhor valor conseguido foi de", memo[top_down(w)], "para o peso de", top_down(w))
