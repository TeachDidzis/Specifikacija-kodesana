import random

def spele():
    nejauss_skaitlis = random.randint(1, 100)
    meginajumi = 10

    print("Esmu iedomājies nejaušu skaitli no 1 - 100. Tavs uzdevums ir to uzminēt ar 10 mēģinājumiem.")
    

    while meginajumi > 0:
        print(f"Atlikušie mēģinājumi: {meginajumi}")
        minejums = int(input("Ievadiet minējumu: "))
        meginajumi -= 1
        if minejums > nejauss_skaitlis:
            print("Mans skaitlis ir mazāks!")
        elif minejums < nejauss_skaitlis:
            print("Mans skaitlis ir lielāks!")
        else:
            print(f"Apsveicam! Jūs uzminējāt pareizo skaitli {nejauss_skaitlis}!")
            break

        if meginajumi == 0 and minejums != nejauss_skaitlis:
            print(f"Jūs zaudējāt. Pareizais skaitlis bija {nejauss_skaitlis}!")
        
    spelet_atkal = input("Vai vēlaties spēlēt atkal? (jā/nē): ")
    if spelet_atkal.lower() == "jā":
        spele()
        

spele()

        
