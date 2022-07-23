# Find the Richest Person
modu = int(input("Enter Modu's money: "))
sodu = int(input("Enter Sodu's money: "))
kodu = int(input("Enter Kodu's money: "))

richest = max(modu, sodu, kodu)
print("The Richest person is", richest)

if modu > sodu and modu > kodu:
    print("Modu is Richest person")
elif sodu > modu and sodu > kodu:
    print("Sodu is Richest person")
else:
    print("Kodu is Richest person")
