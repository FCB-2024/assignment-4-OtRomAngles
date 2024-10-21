def main() :
	number1 = int(input(""))
	i = 1
	sum1 = 0
	sum2 = 0
	y = number1 - 1
	f = 0
	x = number1
	while i <= x:
		if x % i == 0 :
			sum1 = sum1 + 1
		i = i + 1
	while y > 0 :
		i = 1
		sum2 = 0
		while i <= y :
			if y % i == 0 :
				sum2 = sum2 + 1
			i = i + 1
		if sum2 >= sum1 :
			f = 1
		y = y - 1

	if f == 1:
		return("not anti-prime")
	else:
		return("anti-prime")

## DO NOT REMOVE THIS LINE BELOW:
if __name__ == "__main__":
	result = main()
	print(result)

	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
