def num_of_symbols(text):
    symbol_dict = {}
    for s in text:
        if s.isalpha():
            low_s = s.lower()
            if low_s in symbol_dict:
                symbol_dict[low_s] += 1
            else:
                symbol_dict[low_s] = 1
    return symbol_dict

def sort_on(dym_dict):
    return dym_dict[1]

def sort_symbols(dict):
    lst = list(dict.items())
    lst.sort(reverse=True,key=sort_on)
    return lst

def print_stats(lst):
    for v in lst:
        print(f"The '{v[0]}' character was found {v[1]} times")


def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        print(f"--- Begin report of {book} ---")
        file_contents = f.read()
        words = file_contents.split()
        print(f"{len(words)} words was found in the document")
        print(sort_symbols(num_of_symbols(file_contents)))
        print_stats(sort_symbols(num_of_symbols(file_contents)))
        print("--- End report ---")

main()