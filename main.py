import sys
import string

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

USERS = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}

def authenticate(users):
    username = input("username:")
    password = input("password:")
    if username in users and users[username] == password:
        return username
    print("unregistered user, terminating the program..")
    sys.exit()


def select_text(texts):
    print("-" * 40)
    print(f"We have {len(texts)} texts to be analyzed.")
    print("-" * 40)
    choice = input(f"Enter a number btw. 1 and {len(texts)} to select: ")
    if not choice.isdigit():
        print("Invalid input, expected a number, terminating the program..")
        sys.exit()
    idx = int(choice) - 1
    if idx < 0 or idx >= len(texts):
        print("Selected text is out of range, terminating the program..")
        sys.exit()
    return texts[idx]


def clean_words(text):
    words_raw = text.split()
    return [
        w.strip(string.punctuation)
        for w in words_raw
        if w.strip(string.punctuation)
    ]


def analyze_words(words):
    word_count = len(words)
    title_count = sum(1 for w in words if w[0].isupper())
    upper_count = sum(1 for w in words if w.isupper() and w.isalpha())
    lower_count = sum(1 for w in words if w.islower())
    numbers = [int(w) for w in words if w.isdigit()]
    numbers_count = len(numbers)
    numbers_sum = sum(numbers)
    return {
        "word_count": word_count,
        "title_count": title_count,
        "upper_count": upper_count,
        "lower_count": lower_count,
        "numbers_count": numbers_count,
        "numbers_sum": numbers_sum,
    }


def length_frequencies(words):
    freq = {}
    for w in words:
        l = len(w)
        freq[l] = freq.get(l, 0) + 1
    return freq


def print_stats(stats):
    print("-" * 40)
    print(f"There are {stats['word_count']} words in the selected text.")
    print(f"There are {stats['title_count']} titlecase words.")
    print(f"There are {stats['upper_count']} uppercase words.")
    print(f"There are {stats['lower_count']} lowercase words.")
    print(f"There are {stats['numbers_count']} numeric strings.")
    print(f"The sum of all the numbers is {stats['numbers_sum']}.")
    print("-" * 40)


def print_histogram(freq):
    print("LEN| OCCURRENCES           |NR.")
    print("-" * 40)
    for length in sorted(freq):
        count = freq[length]
        stars = "*" * count
        print(f"{length:>3}| {stars:<20} |{count}")


def main():
    username = authenticate(USERS)
    print("-" * 40)
    print(f"Welcome to the app, {username}")
    text = select_text(TEXTS)
    words = clean_words(text)
    stats = analyze_words(words)
    freq = length_frequencies(words)
    print_stats(stats)
    print_histogram(freq)


if __name__ == "__main__":
    main()
