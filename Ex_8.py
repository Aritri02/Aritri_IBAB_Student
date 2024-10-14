def article(w):
    if len(w)==0:
        return False
    first_chr=w[0]
    if first_chr in 'aeiou':
        return True
    else:
        return False
def main():
    w=input("Enter the word: ")
    w = w.lower()
    if article(w):
        print(f"An {w}")
    else:
        print(f"A {w}")
if __name__ == "__main__":
    main()
