# import csv

# def lataa_sanasto(kappale_numero):
#     sanasto = {}
#     tiedostonimi = f"Vocabularies/Chapter_{kappale_numero}.csv"
#     with open(tiedostonimi, encoding='utf-8') as f:
#         for suomi, englanti in csv.reader(f):
#             sanasto[suomi] = englanti
#     return sanasto

import csv

def lataa_sanasto(kappale_tai_tiedosto, tiedostona=False):
    sanasto = {}

    if tiedostona:
        tiedostonimi = f"Vocabularies/{kappale_tai_tiedosto}"

    else:
        tiedostonimi = f"Vocabularies/Chapter_{kappale_tai_tiedosto}.csv"

    try:
        with open(tiedostonimi, encoding='utf-8') as f:
            for suomi, englanti in csv.reader(f):
                sanasto[suomi] = englanti
    except FileNotFoundError:
        print(f"Virhe: Tiedostoa ei löydy: {tiedostonimi}")
        raise

    return sanasto

