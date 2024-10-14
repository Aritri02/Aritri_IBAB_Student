def delimiter(s):
    s=s.replace(",", "and")
    print(s)
def main():
        s = input("Enter the word: ")
        s = s.lower()
        delimiter(s)
if __name__ == "__main__":
        main()
