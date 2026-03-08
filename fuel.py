
while True:
    try:
        frac = input("Fraction: ")
        x,y= frac.split("/")
        x,y=int(x),int(y)
        if x>y or y==0:
            continue
    except ValueError,ZeroDivisionError:
        pass
    else:
        break

percent=round((x/y)*100)
if percent<=1:
    print("E")
elif percent>=99:
    print("F")
else:
    print(f"{percent}%")
