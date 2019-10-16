mas1 = ['E','B','G','H','C','D','F','A']
mas2 = ['A','B','C','D','E','F','G','H']
s = 0
for i in range(0,len(mas1)):
	if mas1[i] != mas2[i]:
		for j in range(0,len(mas1)):
			if mas2[i] == mas1[j]:
				index = j
#				print(index)
		a = mas1[index]
#		print(a)
		mas1[index] = mas1[i]
		mas1[i] = a
#		print(mas1)
		s += 1
	else:
		pass
print(mas1, s)