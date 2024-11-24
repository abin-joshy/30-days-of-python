price=float(input("Enter the total value of your order:"))
if price>=50:
    ship=0
    print("The shipping is free")
elif price<50 and price>=20:
    ship=5
    print("Your shipping cost:$5")
else:
    ship=10
    print("Your shipping cost:$10")
print("The total cost:$",price+ship)