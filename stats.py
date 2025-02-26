from collections import Counter


def count_words(content):
    return len(content.split())

def bookstat(book):
    with open(book) as o:
        c = Counter()
        content = o.read()
        c.update(content.lower())
        wordcount = count_words(content)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{wordcount} words found in the document")
        print("")
        character: str = None
        for character, times in c.items():
            if character.isalpha():
                print(f"{character}: {times}")
        print("--- End report ---")
