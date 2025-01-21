def word_counter(file_contents):
    words = file_contents.split()
    num_words = len(words)
    return num_words


def char_counter(file_contents):
    char_dict = {}
    file_contents = file_contents.lower()

    for char in file_contents:
        if not char in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict


def sort_on(dict):
    return dict["num"]


def sort_dict(char_dict):
    list_of_dicts = []
    for char in char_dict:
        list_of_dicts.append({"char": char, "num": char_dict[char]})

    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts


def report(book, words, dict):
    print(f"--- Begin report of {book} ---")
    print(f"{words} words found in the document\n")
    for element in dict:
        if (
            element["char"] != "\n"
            and element["char"] != " "
            and element["char"] != "#"
            and element["char"] != "."
        ):
            print(f"The '{element["char"]}' character was found {element["num"]} times")
    print("--- End report ---")


def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
    word_count = word_counter(file_contents)
    char_count = char_counter(file_contents)
    char_dict = sort_dict(char_count)
    report(book, word_count, char_dict)


main()
