n = int(input("Enter a number:"))
cout = 0
for i in  range(1 , n+1):
    if n%i == 0:
        cout += 1
if cout == 2:
    print("Prime")
else:
    print("Not Prime")