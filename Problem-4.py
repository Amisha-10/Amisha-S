numbers=list(map(int,input("Enter the numbers seperated by space:").split()))

dict={}

for i in range(1,10):
    count=0
    for num in numbers:
        if num%i==0:
            count+=1
    dict[i] =count

print(dict)

