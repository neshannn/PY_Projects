#Weight Converter
weight = float(input("Enter your weights: "))
unit = input("Kilo grams or pound ? (K or L): ")

if unit == "K":
    weight = weight*2.205
    unit = "Lbs."
elif unit == "L":
    weight = weight/2.205
    unit = "Kgs."
else:
    print(f"{unit} was not a valid option")

print(f"Your weight is :{round(weight, 2)} {unit}")