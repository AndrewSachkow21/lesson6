with open("task1.txt","r") as file:
    ans=[float(x) for x in file.readlines()]
with open("task1.txt","a") as file:
    file.write(str(sum(ans)))
    file.write(str(max(ans)))

    
