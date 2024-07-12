meme_dict = {
    "LOL": "odpowiedź na coś zabawnego",
    "CRINGE": "coś dziwnego lub wstydliwego",
    "ROFL": "odpowiedź na żart",
    "SHEESH": "lekka dezaprobata",
    "CREEPY": "straszny, złowieszczy",
    "AGGRO": "stać się agresywnym/zły"
}

def run_dictionary():
    print("Witaj w aplikacji słownika memów!")
    print("Wpisz słowo, którego znaczenie chcesz poznać (używaj wielkich liter).")
    
    for _ in range(5):
        word = input("\nWpisz słowo: ").upper()
        if word in meme_dict:
            print("Znaczenie '{word}': {meme_dict[word]}")
        else:
            print("Przepraszam, nie znam znaczenia słowa '{word}'.")

    print("Dziękujemy za skorzystanie z aplikacji słownika memów!")

run_dictionary()
