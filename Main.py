import random

sanasto = {
    "koira": "dog",
    "kissa": "cat",
    "auto": "car",
    "pöytä": "table",
    "omena": "apple",
    "koulu": "school",
    "kirja": "book",
    "talvi": "winter",
    "kesä": "summer",
    "vesi": "water"
}

def kysy_sanoja(maara=10):
    pisteet = 0
    kysymykset = random.sample(list(sanasto.items()), maara)

    for suomi, englanti in kysymykset:
        vastaus = input(f"Mikä on englanniksi: {suomi}? ").strip().lower()
        if vastaus == englanti:
            print("✅ Oikein!")
            pisteet += 1
        else:
            print(f"❌ Väärin. Oikea vastaus on: {englanti}")
    
    print(f"\nSait {pisteet}/{maara} oikein.")

# Käynnistetään peli
kysy_sanoja()