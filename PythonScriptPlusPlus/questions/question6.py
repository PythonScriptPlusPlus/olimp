n = int(input())
if n <= 2:
	print('NONE')
	quit()
if n == 5:
	print(0,1)
	quit()
three = 0
four = n // 4
n = n % 4
if n == 2:
	four -= 1
	three = 2
	n = 0
elif n == 1:
	four -= 2
	three = 3
elif n == 3:
	three = 1
print(str(three)+'\n'+str(four))