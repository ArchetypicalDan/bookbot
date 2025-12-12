def count_words(text_content):
    words = text_content.split()
    return len(words)

def count_chars(text_content):
    char_counts = {}
    
    for c in text_content:
        cl = c.lower()
        if cl in char_counts:
            char_counts[cl] += 1
        else:
            char_counts[cl] = 1
    
    return char_counts

def sort_on(items):
    return items["num"]
        
def report_counts(char_counts):
    dict_list = []
    for item in char_counts:
        dict_list.append({"char": item, "num": char_counts[item]})

    return sorted(dict_list, reverse=True, key=sort_on)
    
