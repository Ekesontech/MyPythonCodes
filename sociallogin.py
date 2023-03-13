name = input("Enter name ")
age = int(input("Enter age "))

# multiple conditions
if name == "Alice":
    print("Hello, Alice")
elif age < 12:
    print("you are not Alice, you are a child")
elif age > 2000:
    print("Unlike you, Alice is not an immortal human")
elif age > 100:
    print("You are a grannie and not Alice")
else:
    print("Young blood watch out")