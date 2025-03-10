def get_num_words(path_to_file):
    with open (path_to_file) as f:
        file_contents = f.read()
    num = 0
    words = file_contents.split()
    for word in words:
        num += 1
    return num

def get_num_letters(path_to_file):
    with open (path_to_file) as f:
        file_contents = f.read()
    letters = file_contents.lower()
    tally_dict = {}
    for letter in letters:
        if letter in tally_dict:
            tally_dict[letter] += 1
        else:
            tally_dict[letter] = 1
    return tally_dict

def sort_on(dict):
    return dict["count"]

def sort_letter_counts(tally_dict):
    tally_list = []
    for letter, tally in tally_dict.items():
        tally_list.append({"letter": letter, "count": tally}) 

    tally_list.sort(reverse = True, key = sort_on)
    return tally_list
