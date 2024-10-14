def operations(n1,n2):
    sum=n1+n2
    print(f"The sum of {n1} and {n2} is: {sum}")
    diff=n1-n2
    print(f"The difference of {n1} and {n2} is: {diff}")
    product=n1*n2
    print(f"The product of {n1} and {n2} is: {product}")
    quotient=n1//n2
    print(f"The quotient of {n1} and {n2} is: {quotient}")
    remainder=n1%n2
    print(f"The remainder of {n1} and {n2} is: {remainder}")
def positive_check(prompt):
    while True:
        try:
            value=int(input(prompt))
            if value >0 :
                return value
            else:
                print("Please enter a valid positive number")
        except:
            print("Please enter a non zero positive number")
def main():
    n1=positive_check("Enter the first number: ")
    n2=positive_check("Enter the second number")
    operations(n1,n2)
if __name__ == "__main__":
    main()
