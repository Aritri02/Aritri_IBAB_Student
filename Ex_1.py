import math
def cylinder(r,h):
    volume=math.pi*r*r*h
    return(volume)
def check_positive_input(prompt):
    while True:
        try:
            value=int(input(prompt))
            if value>0:
                return value
            else:
                print("Please enter a positive integer!!")
        except ValueError
def main():
        r=int(input("Enter the radius of the cylinder: "))
        h=int(input("Enter the height of the cylinder: "))
        result=cylinder(r,h)
        print(f"The volume of the cylinder with radius {r} and height {h} is: {result: .2f}")

if __name__ == "__main__":
        main()