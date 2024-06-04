import sys

def get_book_contents(file_path):
    return open(file_path).read()

def get_word_count(word_list):
    word_count = 0
    for word in word_list:
        word_count += 1
    return word_count

def get_character_count(word_list):
    char_count = {}
    for word in word_list:
        for char in word.lower():
            if char not in char_count and char.isalpha():
                char_count[char] = 1
            elif char.isalpha(): 
                char_count[char] += 1
    return char_count

def sort_by_count(dict):
    return dict["count"]

def split_dict(dict):
    entries_list = []
    for key in dict:
        entries_list.append({"char":key, "count":dict[key]})
    return entries_list

def print_report(word_list, file_path):
    word_count = get_word_count(word_list)
    char_count_dict = get_character_count(word_list)
    char_dict_list = split_dict(char_count_dict)
    char_dict_list.sort(reverse=True, key=sort_by_count)

    print(f"--- Report generated for {file_path} ---")
    print(f"{word_count} words found in the document\n")
    for char_dict in char_dict_list:
            print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
    print("\n--- End of report ---")        

def main(file_path):
    book_contents = get_book_contents(file_path)
    word_list = book_contents.split()
    print_report(word_list, file_path)

if __name__ ==  "__main__":

    if len(sys.argv) != 2:
        print("Usage: python main.py <file_path_book.txt>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)
