def median(list):
    sorted_list=sorted(list)
    l=len(sorted_list)
    if l%2!=0:
        return sorted_list[l//2]
    else:
            m1=sorted_list[l//2]
            m2=sorted_list[(l//2)+1]
            m=(m1+m2)/2
            return m
def main():
    list=[]
    n=int(input("Enter the size of the list: "))
    for i in range(0,n):
        elements = int(input("Element: "))
        list.append(elements)
    result=median(list)
    print("The median is: ",result)
if __name__ == "__main__":
    main()




