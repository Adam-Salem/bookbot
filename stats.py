def word_count(text):
    text_list = text.split()
    return len(text_list)

def letter_count(text):
    text = text.lower()
    letter_dict = {}
    for char in text:
        if char not in letter_dict:
            letter_dict[char] = 1
        else:
            letter_dict[char] += 1
    return letter_dict

def dict_sort(letter_dict):
    sorted_dict = list(letter_dict)
    sorted_dict.sort(reverse = True, key = lambda k: letter_dict[k])
    return sorted_dict