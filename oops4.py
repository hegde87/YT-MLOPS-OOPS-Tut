# Why Pyhton is called Object Oriented Programming (OOP)? 
# Everything in Pytho is Object (data structure, data type)
#
class employee:
    def __init__(self):
        print("started executing attributes/data")
        self.id = 123
        self.salary = 5000
        self.designation = "SDE"
        print("attributes/data has been initiated")

    def travel(self, destination):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {destination}")    

# create an object of the class 
sam=employee()

# calling method 
sam.travel("Manglore")         

print (type(sam))
