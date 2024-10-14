def triangle_check(s1,s2,s3):
    if s1+s2>s3 and s2+s3>s2 and s2+s1>s3:
       return True
    else:
        print("Triangle cannot be computed")
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
    s1=positive_check("Enter the first side: ")
    s2=positive_check("Enter the second side: ")
    s3=positive_check("Enter the third side: ")
    if s1==0 or s2==0 or s3==0:
        print("Triangle with side 0 cannot be computed")
    else:
        print(f"Triangle with sides {s1},{s2},{s3} can be formed")
if __name__ == "__main__":
    main()