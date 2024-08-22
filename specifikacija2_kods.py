print("Četrstūra laukuma aprēķināšana!")

while True:
    try:
        while True:
            garums = float(input("Ievadiet četrstūra garumu (cm): "))
            if garums <= 0:
                print("Ievadīts negatīvs skaitlis!")
                continue
            else:
                break
        while True:
            platums = float(input("Ievadiet četrstūra platumu (cm): "))
            if platums <= 0:
                print("Ievadīts negatīvs skaitlis!")
                continue
            else:
                break
        laukums = garums * platums
        print(f"Četrstūra laukums ir {laukums} cm2")
        break
    except ValueError:
        print("Nav ievadīts skaitlis!")

print("\nPaldies par darbu!")


