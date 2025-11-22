def get_num_words(text):
    return len(text.split())

def count_letters(text):
    mydict: dict[str, int] = {}
    text = text.lower()
    for i in text:
        if i in mydict:
            mydict[i] += 1
        else:
            mydict[i] = 0
    return mydict