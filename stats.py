
def get_num_words(file_contents):
    word_list = file_contents.split()
    return len(word_list)

def get_character_count(file_contents):
    character_dic = {}
    for char in file_contents:
        lower_char = char.lower()
        if(lower_char in character_dic):
            character_dic[lower_char] += 1
        else:
            character_dic[lower_char] = 1
    return character_dic

def sort_on(items):
    return items["num"]

def sort_dictionary(character_dict):
    dict_list = []
    for char in character_dict:
        dict_list.append({"char": char, "num": character_dict[char]})
    dict_list.sort(reverse=True, key=lambda x: x["num"])
    return dict_list