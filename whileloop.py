count = 1

while count < 11:
    print("Hello World", count)
    count += 1

    name = ""
while name != "python":
        print("please what is your name ")
        name = input("type here> ")

        started = False
while True:
            print("1. start car, 2. stop car,")
            cmd = input("type here> ")
if cmd == "1":
    if started:
        print("the car is already started")
else:
    started = True
                    