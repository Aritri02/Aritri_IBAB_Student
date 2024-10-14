def triangle(h,b):
    hypo=((h**2)+(b**2))**0.5
    return (hypo)
def positive_check(prompt):
    while True:
        try:
            value=int(input(prompt))
            if value >0:
                return value
            else:
                print("Please enter a positive number!!")
        except ValueError:
            print("Enter a valid number")
def main():
        h = positive_check("Enter the height of the triangle: ")
        b = positive_check("Enter the base of the triangle: ")
        result = triangle(h,b)
        print(f"The hypotenuse of the triangle with height {h} and base {b} is: {result:.3f}")
if __name__ == "__main__":
    main()
