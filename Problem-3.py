a=int(input("Enter the integer:"))
limit=a if a%2!=0 else a-1

for i in range (limit):
    print(2*i+1)

