#   Omar Quirarte       oq5

def main():
    fheight = float(input("Enter your height in FEET: "))
    iheight = float(input("Enter the rest of your height in INCHES: "))
    pounds = float(input("Enter your weight in POUNDS: "))

    #   starting the conversions
    height = float(((fheight * 12) + iheight) * 0.025)
    weight = pounds * 0.45
    height = height * height
    bmi = round(weight / height)

    if (bmi < 18.5):
        print("You are underweight.")
    elif (18.5 <= bmi <= 24.9):
        print("You are normal weight.")
    elif (25 <= bmi <= 29.9):
        print("You are overweight")
    else:
        print("You are obese.")

    print("Your BMI is %d." % bmi)

main()