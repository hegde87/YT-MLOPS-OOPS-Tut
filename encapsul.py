# example 
# In some specific cases , some specific attributes should not be availble for all users
# we dont want all the "users" to access all the attributes/methods which are created by me.
# there could some some attributes which would be sensative [backend -->connecting with DB] [MONGODB--->USERID & PASSWORD]
# This Additional Layer of security is called Encapsulaion in Python.....

#               ========EXAMPLE ========

# ===Go in oops_proj.py ====
# class chatbook:
#     def __init__(self):
#         self.__name = "Default User"                 # this is now become a Hidden Attribute 
#         self.username = ""
#         self.password = ""
  
# ===

from oops_proj import chatbook 
user1 = chatbook()
# print(user1.__name)


# Now if we want to access the Hidden Attribute
# emp(__name) ==> object._classname__attributename 

print(user1._chatbook__name)