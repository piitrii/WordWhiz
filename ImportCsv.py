import csv

def lataa_sanasto(kappale_numero):
    sanasto = {}
    tiedostonimi = f"Vocabularies/Chapter_{kappale_numero}.csv"
    with open(tiedostonimi, encoding='utf-8') as f:
        for suomi, englanti in csv.reader(f):
            sanasto[suomi] = englanti
    return sanasto