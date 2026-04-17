n=int(input("Enter a number to be multiplied:"))
i=int(input("Enter range of multipication table:"))
print("Multiplication table of", n, "is:")
for j in range(1,i+1):
    mul=n*j
    print(n, "x", j, "=", mul)