import sys
def main() :
	num = int(input(""))
	def antiprime(num) :
		sum1 = 0 
		sum2 = 0

		for i in range(1,num+1):
			if num % i == 0:
				sum1 = sum1 + 1
		for i in range(1,num+1):
			sum2 = 0
			for y in range(1,i+1):
				if i % y == 0 :
					sum2 = sum2 + 1
			if sum2 >= sum1 :
				return("not anti-prime")
		return("anti-prime")

	num = int(sys.argv[1])
	result = antiprimecalc(num)
	return result


## DO NOT REMOVE THIS LINE BELOW:
if __name__ == "__main__":

	print(main())
	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
