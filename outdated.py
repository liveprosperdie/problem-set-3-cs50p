
months_list=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input ("Date: ")
    try:
        if "/" in date:
            m,d,y=date.split("/")
            m,d,y= int(m), int(d), int(y) 
            if 0<m<=12 and 0<d<=31:
                print (f"{y}-{m:02}-{d:02}")
                break
            else:
                pass
        elif "," in date:
            m,d,y = date.split(" ")
            d=int(d.strip(","))
            y=int(y)
            if m in months_list:
                m= months_list.index(m) + 1
                if 0<d<=31:
                    print (f"{y}-{m:02}-{d:02}")
                    break
            else:
                pass
        else:
            pass
    except:
        pass

            
