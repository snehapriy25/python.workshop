# class Employee:owner
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def greet(name,age):
#         print("Hello,"+name+"!")

# if __name__=="__main__":
#     name=input("Enter ur name:")
#     age=int(input("Enter ur age:"))
#     Employee.greet(name,age)




class Person:
    def owner(item):
        print(item)

if __name__=="__main__":
    person=str(input("Who are you?"))
    p=Person()

    if person=="owner":
        p.owner()
            
