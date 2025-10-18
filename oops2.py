class employee:
    def __init__(self):
        self.id = 123
        self.salary = 5000
        self.designation = "SDE"

# we have created Class and give attributs [id/salary/designation]
#Note: when ever we are deining any Function inside the Class its called Method 
    def travel(self, destination):
        print(f"Employee is now travelling to {destination}")


# creating Object / instance of the class
sam = employee()       

# print(sam.salary)
# print(sam.id)
sam.travel("goa")

# sam -->employee (class) ==>can access any atribute  