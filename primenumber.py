while True: 
	x = 2
	a = int(input("\nGive me a number (put -1 if you want to stop):"))
	if a == -1:
		break
	while True:
		if a == 2 or a == 3:
			print(a,'is prime')
			break
		if a % x == 0:
			print(a,"is not prime, it is divisible by", x)
			break
		x += 1
		if a % x != 0:
			print(a,'is prime')
			break
