end = []

n = int(input())

if n >= 32:
	n -= 32
	end.append(32)

if n >= 16:
	n -= 16
	end.append(16)

if n >= 8:
	n -= 8
	end.append(8)

if n >= 4:
	n -= 4
	end.append(4)

if n >= 2:
	n -= 2
	end.append(2)

if n >= 1:
	n -= 1
	end.append(1)

print(end)