

def main():
    path_to_file = "books/frankenstein.txt"
    text = read_text(path_to_file)
    word_count = count_words(text)
    alpha_dict = count_characters(text)
    sorted_alpha = sort_dict(alpha_dict)
    print_report(sorted_alpha, word_count)
# read in the text file
def read_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
# count words
def count_words(text):
    return len(text.split())
# count letters
def count_characters(text):
    alphabet_dict = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
    for char in text.lower():
        if char in alphabet_dict:
            alphabet_dict[char] += 1
    
    return alphabet_dict

def sort_dict(alpha_dict):
    sorted_alpha = dict(sorted(alpha_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_alpha

def print_report(sorted_alpha, word_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    for i in (sorted_alpha):
        print(f"The '{i}' character was found {sorted_alpha[i]} times")
    print("--- End report ---")

if __name__ == "__main__":
    main()