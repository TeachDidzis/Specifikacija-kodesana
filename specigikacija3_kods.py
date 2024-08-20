def pasuti_tkreklus(skaits, apdruka, piegade):
    if apdruka.lower() == "teksts":
        cena = 5
    elif apdruka.lower()  == "zīme":
        cena = 7
    elif apdruka.lower()  == "foto":
        cena = 20
    else:
        return f"Nav norādīts pareizs apdrukas veids!"
    
    summa = skaits * cena

    if piegade == True and summa < 50:
        summa += 15

    if summa > 100:
        summa *= 0.95

    return f"{skaits} T-krekli ar apdruku {apdruka} un piegādi maksā {summa} EUR!"

# Testi
print(pasuti_tkreklus(4, "Teksts", True))
print(pasuti_tkreklus(4, "Zīme", True))
print(pasuti_tkreklus(4, "Foto", True))
    