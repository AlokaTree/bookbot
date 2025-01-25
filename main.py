#!/usr/bin/python3

def main():
    print("--- Begin report of books/frankenstein.txt ---")
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document" "\n")
    chars_dict = get_chars_dict(text)
    letters_found = get_letters(chars_dict)
    print("--- End report ---")
    
#    print(letters_found)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_letters(chars_dict):
#    new_dict = []
    for key, value in sorted(chars_dict.items()):
        if key.isalpha() == True:
            #new_dict.append({key:value})
            print(f"the '{key}' character was found {value} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()