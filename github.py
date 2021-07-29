def sum():
	sum=0
	extent=int(input("Enter limit: "))
	for i in range(0,extent):
		num=int(input("Enter number: "))
		sum=sum+num	
	return sum

def main():
	print(sum())
if __name__=="__main__":
	main()
