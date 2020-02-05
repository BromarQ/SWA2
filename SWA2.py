#   Omar Quirarte          oq5

def main():
    print("Enter a number to run the BMI function, Retirement plan, or quit the program.")
    choice = int(input("Type 1 for BMI, 2 for Retirement, or 3 to quit: "))

    if (choice == 1):
        BMI()
    elif (choice == 2):
        Retirement()
    elif (choice == 3):
        print("Have a good day!")
        quit()
    else:
        print("Error: Enter either 1 or 2.")
        main()

    print("Would you like to run one of these functions again?")
    choice2 = int(input("Enter 1 for BMI, 2 for Retirement, or 3 to quit: "))
    if (choice2 == 1):
        BMI()
    elif (choice2 == 2):
        Retirement()
    elif (choice2 == 3):
        print("Have a good day!")
        quit()
    else:
        print("Error: Enter either 1, 2, or 3.")
        main()

def BMI():
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
    return

def Retirement():
    age = int(input("Enter your age: "))
    asal = float(input("Enter your annual salary: "))
    percSave = float(input("Enter your percentage saved: "))
    goal = float(input("Enter your desired retirement savings goal: "))

    #   calculations start
    percSave = percSave / 100

    save = percSave * asal

    employer = 0.35 * save

    totalSave = employer + save
    savings = totalSave

    while (savings < goal):
        age = age + 1
        savings = savings + totalSave
        if (age >= 100):
            print("You do not reach your savings goal.")
            break

    if (savings >= goal):
        print("You met your savings goal at age %d" % age)
    return


main()