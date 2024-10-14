def prime(n):
    if n==1:
        print(f"{n} is a special number")
    else:
        for i in range (2,int(n**0.5)+1):
            if n%i==0:
                print(f"{n} is a composite number")
                return False
        return True
def main():
    n= int(input("Enter the number: "))
    if prime(n):
        print(f"{n} is a prime number")
if __name__ == "__main__":
    main()


