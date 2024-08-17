def main():
    book_file_path = "books/frankenstein.txt"
    book_text = get_book(book_file_path)
    book_word_count = get_word_count(book_text)
    book_character_count = get_character_count(book_text)
    sorted_character_list = sort_dictionary_list(book_character_count)
    print(f"--- Character report for {book_file_path} ---")
    print(f"{book_word_count} words were found.")
    for char in sorted_character_list:
        if not char["character"].isalpha():
            continue
        print(f"The '{char['character']}' character was found {char['count']} times!")
    print(f"--- End character report ---")

def get_book(path):
    with open(path) as f:
        text = f.read()
        return text

def get_word_count(text):
    word_array = text.split()
    word_count = len(word_array)
    return word_count

def get_character_count(text):
    characters = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char in characters:
            characters[lowered_char] += 1
        else:
            characters[lowered_char] = 1
    return characters

def get_dictionary_list(chars):
    return chars["count"]

def sort_dictionary_list(dict):
    sorted = []
    for char in dict:
        sorted.append({"character": char, "count": dict[char]})
    sorted.sort(reverse=True, key=get_dictionary_list)
    return sorted

main()
