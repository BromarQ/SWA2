#   Omar Quirarte       oq5

def main():
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



main()