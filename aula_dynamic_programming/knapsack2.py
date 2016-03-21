# -*- coding: utf-8 -*-

W = 10
P = [(5,5), (3,2), (1,0), (10,6), (8,5)]

# Solve each case.
F = [(0, -1)]
for w_total in range(1, W + 1):
    # Solve this case.
    best_item = (0, -1)
    best_bag_value = -1
    for w, v in P:
        w_left = w_total - w
        if w_left >= 0:
            this_bag_value = v + F[w_left][1]
            if this_bag_value > best_bag_value:
                best_bag_value = this_bag_value
                best_item = (w, v)
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
