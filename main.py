from collections import Counter

def main():
    with open('./books/frankenstein.txt') as o:
        c = Counter()
        content = o.read()
        c.update(content.lower())
        wordcount = len(content.split())
        # print(content)
        # print(wordcount)
        # print(c)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{wordcount} words found in the document")
        print("")
        character: str = None
        for character, times in c.items():
            if character.isalpha():
                print(f"The '{character}' character was found {times} times")
        print("--- End report ---")

main()