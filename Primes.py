def isPrimes(num):
	if num<1:
		print(num,'not prime')
	else:
		x = num//2
		while x>1:
			if num % x ==0:
				print(num,'has factor',x)
				break
			x -= 1
		else:
			print(num,'is prime')
			
isPrimes(13)
isPrimes(13.0)
isPrimes(15)
isPrimes(15.0)
isPrimes(0)
isPrimes(-1)