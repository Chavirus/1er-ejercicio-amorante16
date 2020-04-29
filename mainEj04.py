
# DO NOT MODIFY THE CODE BELOW THIS LINE
def main():
# DO NOT MODIFY THE CODE ABOVE THIS LINE
    # Program should start here
    n1 = int(input("Ingrese número 1: "))
    n2 = int(input("Ingrese número 2: "))
    n3 = int(input("Ingrese número 3: "))
    n4 = int(input("Ingrese número 4: "))

    temp=n1
    if n2<n1:
        temp =n2
        n2 = n1
        n1 = temp
    if n3 < n2:
        temp =n3
        n3 = n2
        n2 = temp
        if n2<n1:
            temp =n2
            n2 = n1
            n1 = temp
    if n4 < n3:
        temp = n4
        n4 = n3
        n3= temp
        if n3 < n2:
            temp =n3
            n3 = n3
            n2 = temp
            if n2<n1:
                temp =n2
                n2 = n1
                n1 = temp
    print(f"Ordenados: {n1} {n2} {n3} {n4}")

    # Program should end here
def bar():
    ans = input("enter yes or no")
    if ans == "yes":
        return "you entered yes"
    if ans == "no":
        return "you entered no"

# DO NOT MODIFY THE CODE BELOW THIS LINE
if __name__ == '__main__':
    main()
# DO NOT MODIFY THE CODE ABOVE THIS LINE
