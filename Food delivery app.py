print("wlecome to food fiasta")
print("""1.mass hotel
2.grand hotel""")

totalprice=0
hotel=int(input("enter your hotel 1 or 2:")) # to choose which hotel to select
if hotel==1:
    print("""wlicome to mass hotel""")
    print("1.mb\n2.cb\n3.chiken 65\n4.lollypop")
    mb=200
    cb=180
    cc=140
    lp=100
    price=0
    totalprice=0

    while hotel!=0: 
        totalprice+=price  # to calculate total amount by adding each iteam
        menu=int(input("enter the item number: "))
        if menu==1:
            quantity=int(input("enter the quantity: "))
            price=200*quantity
            print(price)

        if menu==2:
             quantity=int(input("enter the quantity: "))
             price=180*quantity
             print(price)
        if menu==3:
            quantity=int(input("enter the quantity: "))
            price=80*quantity
            print(price)
        if menu==4:
            quantity=int(input("enter the quantity: "))
            price=10*quantity
            print(price)
        if menu==0:
            break
if hotel==2:
    print("""wlicome to mass hotel""")
    print("1.mb\n2.cb\n3.chiken 65\n4.lollypop")
    mb=200
    cb=180
    cc=140
    lp=100
    price=0
    totalprice=0

    while hotel!=0: 
        totalprice+=price  # to calculate total amount by adding each iteam
        menu=int(input("enter the item number: "))
        if menu==1:
            quantity=int(input("enter the quantity: "))
            price=200*quantity
            print(price)

        if menu==2:
             quantity=int(input("enter the quantity: "))
             price=180*quantity
             print(price)
        if menu==3:
            quantity=int(input("enter the quantity: "))
            price=80*quantity
            print(price)
        if menu==4:
            quantity=int(input("enter the quantity: "))
            price=10*quantity
            print(price)
        if menu==0:
            break

print("your total price is",totalprice)

s=input("do you wish to continue payment (yes/no): ")
if s=="yes":
    mode=input("enter your mode of payment upi/cod/card: ")
    if mode=="upi":
        print("payment done\norder placed sucessfully")
    elif mode=="card":
        print("payment done\norder placed sucessfully")
    elif mode=="cod":
        print("payment done\norder placed sucessfully") 
    else:
        print("enter valid mode upi/cod/card")

