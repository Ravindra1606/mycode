def main():
    print("Simple and Compound Interest Calculator")
    print("1. Simple Interest")
    print("2. Compound Interest")
    choice = int(input("Enter your choice (1 or 2): "))
    if choice == 1:
        p = float(input("Enter the principal amount: "))
        r = float(input("Enter the rate of interest: "))
        t = float(input("Enter the time (in years): "))
        si = (p * r * t) / 100
        print("Simple Interest:", si)
    elif choice == 2:
        p = float(input("Enter the principal amount: "))
        r = float(input("Enter the rate of interest: "))
        t = float(input("Enter the time (in years): "))
        n = int(input("Enter the number of times the interest is compounded in a year: "))
        ci = p * (pow((1 + (r / n)), (n * t)))
        print("Compound Interest:", ci)
    else:
        print("Invalid Choice")

if __name__ == '__main__':
    main()







