##counting fro 1 to 10
for i in range(1,11):
    print("Count:",i)
## reverse conting:    
for i in range(1, 11):
    print("reverse count:",i)
## even numbers
for i in range(0,21,2):
    print("Even Numbers:",i)
## sun of numbers
n = int(input("Enter a number: "))
total = 0
for i in range(1, n):
    total = total + i
print("Sum:", total)
##multiplication
n=int(input("enter your n vlaue:"))
mul=1
for i in range(1,11):
    for j in range(1,11):
        print(f"Mul:{i}*{j}")