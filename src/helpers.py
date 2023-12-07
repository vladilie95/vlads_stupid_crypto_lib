
ALPHABET_SIZE = 26

def map_to_26(text):
    mapped_list = []
    for letter in text:
        if letter >= "A" and letter <= "Z":
            mapped_list.append(ord(letter) - ord("A"))
        else:
            mapped_list.append(-1)
    return mapped_list

def map_to_letter(number):
    if number >= 0 and number <= 26:
        return chr(ord("A") + number)
    return chr(0)
    
            
