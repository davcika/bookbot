def get_num_words(text):
    return len(text.split())

def count_letters(text):
    mydict: dict[str, int] = {}
    text = text.lower()
    for i in text:
        if i in mydict:
            mydict[i] += 1
        else:
            mydict[i] = 1
    return mydict

def pretty_sort(dict_s):
    sorted_dict = dict(sorted(dict_s.items(), key=lambda item:item[1], reverse=True))
    return sorted_dict
    
def pretty_print(path, word_count, sorted_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in sorted_dict:
        print(f"{i}: {sorted_dict[i]}")
    print("============= END ===============")
