#n * n-1 * n-2 * ....1

num = int(input("Number:"))
factorial = 1

if num < 0:
	print("fatorial = 1")
elif num == 0:
	print("factorial = 1")
else:
	for i in range(1,num + 1):
		factorial = factorial * i
print(factorial)