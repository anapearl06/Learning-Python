# Delivery Charge Calculator

distance = float(input("Enter delivery distance (in km): "))

if distance <= 2:
    print("Delivery charge: 0")
elif distance <= 5:
    print("Delivery charge: 30")
elif distance <= 10:
    print("Delivery charge: 50")
else:
    print("Delivery not available for your location.")