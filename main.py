group = list()
cont = True#continue
mod = int(input("Enter your mod number"))
order = 0
primitve = int(input("Enter your primitive element"))
k = True
def isCyclicg():
    global k
    cardinality = len(group)
    global order
    i = 1
    while k:
        if ((primitve**i)% mod == 1):
            order += 1
            print((primitve**i)% mod)
            if(order==cardinality):
                print("This Group is Cycling")
                print("Cardinality : "+str(cardinality)+" Order : " +str(order))
                return True
            else:
                print("This Group is not Cycling")
                print("Cardinality : "+str(cardinality)+" Order : " +str(order))
                return False
            k = False
        else:
            print((primitve ** i) % mod)
            order +=1
        i+=1

while cont:
    item = input("Enter your group's items if you want to exit please write exit and press enter")
    if(item == "exit"):
        cont = False
    else:
        group.append(item)

isCyclicg()