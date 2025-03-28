def count_words(text):
    return len(text.split())

def count_chars(text):
    char_dict = {}
    text =  text.lower()
    for char in text:
        char_dict[char]=char_dict.get(char,0)+1
    return char_dict

def get_sorted_list(dict):
    return sorted([kv for kv in dict.items() if kv[0].isalpha()], key= lambda kv: (kv[1],kv[0]),reverse=True)
