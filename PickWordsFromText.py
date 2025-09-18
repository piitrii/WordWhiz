import csv
from google import genai
from google.genai import types

client = genai.Client()

# Teksti
#sample_text = input("Anna teksti sanakoetta varten: ")

# Funktio, joka hakee tärkeimmät sanat
def get_keywords_from_text(text, num_words=10):
    prompt = f"""
    Analyze the following English text and extract the {num_words} most important or relevant words for a vocabulary test. Use only the base form of the extracted words and their translations.
    Return the result as lines in the format: finnish_translation,english_word

    Only return the list. No explanations.
    Only extract words that can be found in text.
    
    Text:
    {text}
    """
    response = client.models.generate_content(model="gemini-2.5-flash-lite", contents=prompt)
    lines = response.text.strip().split('\n')

    result = []
    for line in lines:
        if ',' in line:
            parts = line.split(',')
            if len(parts) >= 2:
                eng = parts[0].strip()
                fin = parts[1].strip()
                result.append((eng, fin))
    return result

# Funktio, joka tallentaa CSV-tiedostoon
def save_to_csv(word_list, filename):
    if not filename.endswith(".csv"):
        filename += ".csv"
    filepath = f"Vocabularies/{filename}"
    with open(filepath, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(word_list)
    print(f"Tiedosto tallennettu: {filepath}")

def pick_words_interactive():
    sample_text = input("Anna teksti sanakoetta varten: ")
    keywords = get_keywords_from_text(sample_text)
    print("10 tärkeintä sanaa ja niiden suomennokset:")
    for fin, eng in keywords:
        print(f"{fin},{eng}")
    filename = input("\nAnna CSV-tiedoston nimi (ilman .csv-päätettä): ")
    save_to_csv(keywords, filename)

# Suoritus
#keywords = get_keywords_from_text(sample_text)

# Tulosta ja tallenna
#print("10 tärkeintä sanaa ja niiden suomennokset:")
#for fin, eng in keywords:
#    print(f"{fin},{eng}")

# Kysy tiedoston nimi ja tallenna
#filename = input("\nAnna CSV-tiedoston nimi (ilman .csv-päätettä): ")
#save_to_csv(keywords, filename)