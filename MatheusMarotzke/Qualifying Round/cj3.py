import math
from random import randrange
import time
import itertools as it

#http://stackoverflow.com/questions/18833759/python-prime-number-checker
def is_prime_1(n):
    if n == 2:
        return True
    if (n < 2) or (n % 2 == 0):
        return False
    return not any(n % i == 0 for i in range(3, int(math.sqrt(n)) + 1, 2))

def is_prime_2(n, k=10):
	if n == 2:
		return True
	if not n & 1:
		return False

	def check(a, s, d, n):
		x = pow(a, d, n)
		if x == 1:
			return True
		for i in range(s - 1):
			if x == n - 1:
				return True
			x = pow(x, 2, n)
		return x == n - 1

	s = 0
	d = n - 1

	while d % 2 == 0:
		d >>= 1
		s += 1

	for i in range(k):
		a = randrange(2, n - 1)
		if not check(a, s, d, n):
			return False
	return True

with open("output2.txt", "w") as out:
	num = 32
	n = 500
	r = [[0,1]]*30
	lista = []
	out.write("Case #1:\n")
	cont = 0
	for item in it.product(*r):
		if cont == n:
			break
		now = time.time()
		itens = []
		itens.append(1)
		for k in item:
			itens.append(k)
		itens.append(1)

		soma = []
		for i in range(2,11):
			somap = 0
			j = len(itens)-1
			for ind in itens:
				if ind == 1:
					somap += ind*(i**j)
				j -= 1
			
			if somap == 0:
				break

			if is_prime_2(somap):
				break

			soma.append(somap)


		if len(soma) == 9:
			final = []
			future = True
			isso = True
			while future:
				for s in soma:
					if s%2 != 0:
						for r in range(3,math.ceil(math.sqrt(s)),2):
							if time.time() > now + 0.5:
									print('time_out')
									future = False
									break
							if s%r == 0:
								final.append(r)
								break
					else:
						final.append(r)

				if len(final) == 9:
					
					f = ''
					for u in final:
						f += str(u)
						f += ' '
					h = ''
					for e in itens:
						h += str(e)

					if not h in lista:
						lista.append(h)
						out.write("{0} {1}\n".format(h,f))

						cont +=1
						print(cont)
						future = False

