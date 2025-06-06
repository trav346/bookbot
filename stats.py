def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    text = text.lower()
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_characters(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        if char.isalpha():  # only count letters
            sorted_list.append({"char": char, "num": count})
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list
