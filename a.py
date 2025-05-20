def sum(a,b):
    return a+b

def difference(a,b):
    return a-b

def product(a,b):
    return a*b

def division(a,b):
    return a/b

print("Select operation")
print("1.Sum \t 2.difference \t 3.Product \t 4.division")

a=int(input("Enter a:"))
b=int(input("Enter b:"))

if(a>b):
    print(sum(a,b))
    
elif(a<b):
    print(difference(a,b))

elif(a==b):
    print(product(a,b))

elif(a>=b):
    print(division(a,b))

else:
    print("invalid input")