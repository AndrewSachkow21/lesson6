with open("task1.txt","w") as file:
    list = input(":").split()
    for i in list:
        file.write(i+"\n")
