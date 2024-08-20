print("Četrstūra laukuma aprēķināšana!")

while True:
    try:
        garums = float(input("Ievadiet četrstūra garumu (cm): "))
        if garums <= 0:
            print("Ievadīts negatīvs skaitlis!")
            continue
        platums = float(input("Ievadiet četrstūra platumu (cm): "))
        if platums <= 0:
            print("Ievadīts negatīvs skaitlis!")
            continue
        else:
            laukums = garums * platums
            print(f"Četrstūra laukums ir {laukums} cm2")
            break
    except ValueError:
        print("Nav ievadīts skaitlis!")

print("\nPaldies par darbu!")

