    # :::::: NOTE ::::::
# Getter :- Get the hidden Attribute    i.e we have kept ==> get_name   in line 16
# Setter :- Set the hidden Attribute    i.e we have kept ==> set_name   in line 19

# In oops_proj.py file we have added 2 

# class chatbook:
#     def __init__(self):
#         self.__name = "Default User"   # this is the hidden attribute .....for this will create getter and setter 
#         self.username = ""
#         self.password = ""
#         self.loggedin = False
#         # self.menu()
        
# # creating a getter and setter for the hidden attribute i.e line 3
#     def get_name(self):
#         return self.__name
    
#     def set_name(self, value):
#         self.__name = value        
 
# getter and setter
from oops_proj import chatbook
user1 = chatbook()          #   Created Object 
print(user1.get_name())     #   According to the object checked the name 
user1.set_name('Agent XXX') #   we gave a new name 
print(user1.get_name())     #   Again checking the name If the name is set 