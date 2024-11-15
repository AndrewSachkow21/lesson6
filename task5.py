with open("task5.txt","r") as file:
    places_count = 0 
    ans=[g for g in[x.split() for x in file.readlines()]]
    for x in ans:
        for i in x:
            if "0" is i:
                places_count += 1
    print("вільниx місць:",places_count)
    place=[int(i)-1 for i in input("ряд та стовпець через пробіл:").split()]
    if ans[place[0]][place[1]] is "0":
        print("це місце незайняте")
    else:
        print("це місце зайняте")
print("2" == 2)
