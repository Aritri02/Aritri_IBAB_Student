def color_check(w):
    if w>=380 and w<450:
        print("VIOLET")
    elif w>=450 and w<495:
        print("BLUE")
    elif w>=495 and w<570:
        print("GREEN")
    elif w >= 570 and w < 590:
        print("YELLOW")
    elif w>=590 and w<620:
        print("ORANGE")
    elif w>=620 and w<750:
        print("RED")
    else:
        print("Wavelength not in range")
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
    w=positive_check("Enter the wavelength in nm: ")
    if w<0 or w>750:
        print("This value does not represent wavelength in nanometers")
    else:
        color_check(w)
if __name__ == "__main__":
    main()
