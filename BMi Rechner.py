if __name__ == "__main__":
    print("Willkommen!")
    name = input("Bitte geben Sie ihren Namen ein: ")
    weight = int(input("Bitte geben Sie ihr Gewicht ein: "))
    height = float(input("Bitte geben Sie ihre Größe in Metern ein: "))
    bmi = (weight/(height**2))
    print("Hallo " + name + ", dein BMI lautet: " + str(bmi))
    if bmi < 18.5:
        print("Dein BMI ist unterdurchschnittlich")
    elif 18.5 <= bmi <= 25:
        print("Dein BMI ist Normal")
    elif bmi > 25:
        print("Dein BMI ist überdurchschnittlich")
    else: 
        pass
    
    