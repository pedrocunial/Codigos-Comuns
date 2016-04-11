a = [3, 2, 3]
n = len(a)

b = [0] * n

really_done = False
while not really_done:
    print(b)
    # Adicionar 1 em b
    done = False
    k = 0
    while not done:
        done = True
        b[k] += 1
        if b[k] == a[k]:
            b[k] = 0
            k += 1
            if k < len(a):
                done = False
            else:
                really_done = True
                
