from ImportCsv import lataa_sanasto
from AskWords import kysy_sanoja

def main():
    print("Tervetuloa sanapeliin!")
    print("Valitse kappale:")
    for i in range(1, 6):
        print(f"{i}. Kappale {i}")
    valinta = int(input("Valintasi: "))
    
    sanasto = lataa_sanasto(valinta)
    kysy_sanoja(sanasto)

if __name__ == "__main__":
    main()