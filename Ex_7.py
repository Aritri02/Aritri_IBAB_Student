def operations(n):
    square=n**2
    print(f"The square of {n} is: {square}")
    cube=n**3
    print(f"The cube of {n} is: {cube}")
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
    n=positive_check("Enter the number: ")
    operations(n)
if __name__ == "__main__":
    main()
