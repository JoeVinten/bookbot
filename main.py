
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_counts = get_each_char_count(text)
    print_report(book_path, word_count, char_counts)

def print_report(path, word_count, char_count):
    print(f'********* Begin report of {path} *********\n')
    print(f'{word_count} words in the document\n')
    print_char_occurrences(sort_by_number(char_count))
    print(f'********* End report *********\n')

def get_book_text(path):
    with open (path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words) + 1;

def get_each_char_count(text):
    chars_dict = {}
    for char in text: 
        lowered = char.lower()
        if lowered not in chars_dict:
            chars_dict[lowered] = 1
        else:
            chars_dict[lowered] += 1
    return chars_dict


def sort_on(d):
    return d["count"]

def sort_by_number(dict_values):
    sorted_list = []
    for char in dict_values:
        if char.isalpha():
            sorted_list.append({"char": char, "count": dict_values[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def print_char_occurrences(char_list):
    for char_dict in char_list:
        print(f'The {char_dict["char"]} was found {char_dict["count"]} times')


main()
