def median(n1,n2,n3):
    n=(n1,n2,n3)
    sorted_numbers=sorted(n)
    return sorted_numbers[1]
def positive_check(prompt):
    while True:
        try:
            value=int(input(prompt))
            if value>0:
                return value
            else:
                print("Please enter a positive number")
        except:
            print("Enter a valid positive number")
def main():
    n1 = positive_check("Enter the first number: ")
    n2 = positive_check("Enter the second number: ")
    n3= positive_check("Enter the third number: ")
    result = median(n1,n2,n3)
    print(f"The median of {n1}, {n2} and {n3} is: {result}")
if __name__ == "__main__":
    main()