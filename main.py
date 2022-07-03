n = int(input("Please enter a positive integer: "))
print("The factors of", n, "are:")
for i in range(2, n):
    if n % i == 0:
        print(i)
