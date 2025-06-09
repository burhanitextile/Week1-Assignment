n = int(input("Enter the number of rows: "))

def lower_triangle(n):
    for i in range(1, n+1):
        print("*" * i)


def upper_triangle(n):
    for i in range(1, n):
        space = n-i
        print(" " * space + "*" * i)


def pyramid(n):
    for i in range(1, n):
        space = n-i
        star = 2*i-1
        print(" " * space + "*" * star)


print("Lower Triangle")
lower_triangle(n)
print()

print("Upper Triangle")
upper_triangle(n)
print()

print("pyramid")
pyramid(n)
print()