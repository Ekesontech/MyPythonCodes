db_name = "mary"
db_password = "swordfish"

u_name = input ("Enter username: ")
u_pwd = input ("Enter password: ")


if u_name.lower() == db_name:
    if u_pwd == db_password:
        print("Access granted!!")
    else:
        print("Access Denied.")
        print("Username or password incorrect")

else:

    print("No match found!!")
print("Outside of all indent") 

