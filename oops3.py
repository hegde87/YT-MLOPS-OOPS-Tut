
# here,
# we created Class 
# how did we define data/attribute 
# how did we write a method inside a class 
# how we created a Object 
# how we called the object using the class 
# once object is created then the attribute gets called automatically 
# Functions or method have to be called manually -->it does not get called automatically. 

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