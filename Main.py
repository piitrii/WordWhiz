# from ImportCsv import lataa_sanasto
# from AskWords import kysy_sanoja

# def main():
#     print("Tervetuloa sanapeliin!")
#     print("Valitse kappale:")
#     for i in range(1, 6):
#         print(f"{i}. Kappale {i}")
#     valinta = int(input("Valintasi: "))
    
#     sanasto = lataa_sanasto(valinta)
#     kysy_sanoja(sanasto)

# if __name__ == "__main__":
#     main()

from ImportCsv import lataa_sanasto
from AskWords import kysy_sanoja

# Jos ohjelmaa ajaa terminaalin kautta, niin tulee ensin mennä WordWhiz-kansioon, jotta ohjelma löytää ennakkoon muodostetut sanastot Chapter_1.csv jne. 
def main():
    print("Tervetuloa sanapeliin!")
    print("Valitse vaihtoehto:")
    print("1–5: Käytä valmista sanastoa kappaleen syöttämällä haluamasi kappaleen numero")
    print("T: Anna oma CSV-tiedosto, jonka tekstistä sanat poimitaan (esim. sanakoe.csv)")

    valinta = input("Valintasi: ").strip()

    if valinta.lower() == "t":
        tiedostonimi = input("Anna CSV-tiedoston nimi: ").strip()
        try:
            sanasto = lataa_sanasto(tiedostonimi, tiedostona=True)
        except FileNotFoundError:
            print(f"Tiedostoa '{tiedostonimi}' ei löytynyt.")
            return
    else:
        try:
            num = int(valinta)
            if not 1 <= num <= 5:
                print("Valitse numero 1–5.")
                return
            sanasto = lataa_sanasto(num)
        except ValueError:
            print("Virheellinen valinta.")
            return

    kysy_sanoja(sanasto)

if __name__ == "__main__":
    main()