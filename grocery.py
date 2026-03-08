gr_list={}
while True:
    try:
        item=input()
        if item not in gr_list:
            gr_list[item] = 1
        else :
            gr_list[item] +=1
    except EOFError:
        break

list=sorted(gr_list)

for i in list:
    print(gr_list[i], i.upper() ) #list and dictionary both are used
