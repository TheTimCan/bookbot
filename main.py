def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        word_count = get_word_count(file_contents)
        char_counts = get_char_counts(file_contents)
        sorted_chars = []
        for k, v in char_counts.items():
            if k.isalpha():
                sorted_chars.append({'char': k, 'num': v})
        sorted_chars.sort(key=lambda k: k['num'], reverse=True)

        for i in sorted_chars:
            print(f"The letter {i['char']} appeared {i['num']} times")

        print(f"Word count: {word_count}\n")


def get_word_count(file):
    return len(file.split())


def get_char_counts(file):
    char_dict = {}
    lowered_text = file.lower()
    for word in lowered_text:
        for char in word:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict


main()
