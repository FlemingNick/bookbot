def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    chars = {}
    for char in text:
        if not char.lower() in chars:
            chars[char.lower()] = 1
        else:
            chars[char.lower()] += 1
    return chars

def sort_on(items):
    return items["char"]

def print_report(dict):
    newList = sorted(list(dict.items()), key=lambda x: x[1], reverse=True)
    
    
    for key, value in newList:
        print(f"{key}: {value}")
            