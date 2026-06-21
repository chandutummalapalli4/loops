## Factorial of Number
n=int(input("Enter a Number:"))
fact=1
for i in range(1,n):
    fact=fact*i
print("Factorial of Number:",fact)
## using while
n=int(input("Enter a Number:"))
fact=1
i=1
while i<=n:
    fact=fact*i
    i+=1
print(fact)