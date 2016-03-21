# -*- coding: utf-8 -*-

W = 10
P = [(5,5), (3,2), (1,0), (10,6), (8,5), (1,2)]

# Solve each case.
F = []
for w_total in range(W + 1):
    # Solve this case.
    best_item = (0, 0)
    best_bag_value = 0
    for w, v in P:
        w_left = w_total - w
        if w_left >= 0:
            this_bag_value = v + F[w_left][1]
            if this_bag_value > best_bag_value:
                best_bag_value = this_bag_value
                best_item = (w, best_bag_value)
    F.append(best_item)

# Backtrack.
bag = []
w = W
c = 0
while w > 0:
    item = F[w]
    bag.append(item[0])
    w -= item[0]

print(F)
print(bag)
