prihlasovaci_udaje = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
}
jmeno = input("Zadej své uživatelské jméno: ")
heslo = input("Zadej své heslo: ")
if jmeno in prihlasovaci_udaje:
    if prihlasovaci_udaje[jmeno] == heslo:
        print(f"Vítej, {jmeno} \nNyní můžeš analyzovat své texty.")
    else:
        print("Nesprávné heslo.")
        quit()
else:
    print("Nejsi registrovaný. Ukončuji program.")
    quit()
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]
vybrany_text = int(input("Zadej číslo textu, který chceš analyzovat:"))
pocet_textu = len(TEXTS)
if 1 <= vybrany_text <= pocet_textu:
    tenhle_text_analyzuj = TEXTS[vybrany_text-1]
    print(f"Vybral/a jsi si text číslo {vybrany_text}: {tenhle_text_analyzuj}")
    pro_jistotu = input(f"Chceš analyzovat tento text? (ano/ne):")
    if pro_jistotu == "ano":
        slova = tenhle_text_analyzuj.split()
        pocet_slov = len(slova)
        zacinajici_velce = []
        capslock = []
        cisla = []
        for slovo in slova:
            if slovo.istitle():
                zacinajici_velce.append(slovo)
            elif slovo.isupper():
                capslock.append(slovo)
            elif slovo.isdigit():
                cisla.append(int(slovo))
        pocet_slov_zacinajicich_velce = len(zacinajici_velce)
        pocet_capslock = len(capslock)
        kolik_cisel = len(cisla)
        pocet_mini = pocet_slov - pocet_slov_zacinajicich_velce - pocet_capslock - kolik_cisel
        soucet = sum(cisla)
        graf = {}
        for slovo in slova:
            fakt_slova = slovo.strip(""".,?!:;/"'""")
            pocet_znaku = len(fakt_slova)
            if pocet_znaku > 0:
                if pocet_znaku in graf:
                    graf[pocet_znaku] = graf[pocet_znaku] + 1
                else:
                    graf[pocet_znaku] = 1
        print(f"Tebou vybraný text obsahuje {pocet_slov} slov.\nZ toho {pocet_slov_zacinajicich_velce} začíná na velké písmeno,\n{pocet_capslock} je psáno/jsou psány velkými písmeny,\n{pocet_mini} pouze malými,\ntext obsahuje {kolik_cisel} čísla/čísel \na součet všech čísel je {soucet}.")
        print("Zde je graf zobrazující četnost jednotlivých délek slov:")
        serazene = sorted(graf.keys())
        for pocet_znaku in serazene:
            kolikrat = graf[pocet_znaku]
            hvezdicky = "*" * kolikrat
            print(f"\n{pocet_znaku}|{hvezdicky} {kolikrat}")    
    elif pro_jistotu == "ne":
        print(f"\nVýše vidíš texty, ze kterých můžeš vybírat.\nUkončuji program.{print(TEXTS)}")
        quit()
    else:
        print(f"Nezadal/a jsi odpověď ve formátu ano/ne.\nUkončuji program.")
        quit()
else:
    print(f"Text s tímto číslem neexistuje, nebo jsi nezadal/a číslo. Můžeš zadat číslo od 1 do {pocet_textu}.\nUkončuji program.")
    quit()