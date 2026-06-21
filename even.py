for i in range(0,21,2):
    print("Even Numbers:",i)
## 2 method
n=int(input("Enter a number:"))
i=1
for i in range(n):
    if i%2==0:
        print(i)
## for odd numbers
n=int(input("Enter a number:"))
i=1
for i in range(n):
    if i%2!=0:
        print(i)