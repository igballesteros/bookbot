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


def list_dict(char_dict):
    list_of_dicts = []
    for char in char_dict:
        list_of_dicts.append({"char": char, "num": char_dict[char]})

    sort_on(list_of_dicts)


# def report(word_counter, char_counter):


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = word_counter(file_contents)
    char_count = char_counter(file_contents)
    list_dict(char_counter(file_contents))


main()
