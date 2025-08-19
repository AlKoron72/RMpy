import string

all_letters = list(string.ascii_letters)

def encrypt(this_string: str, direction: int) -> str:
    return_string = ""
    
#    map = str.maketrans(" _", "_ ")
#    direction.trandlate(map)

    for letter in this_string:
        l_index = all_letters.index(letter)
        
        if l_index + direction >= len(all_letters):
            l_index -= len(all_letters)
        elif l_index + direction < 0:
            l_index += len(all_letters)
        
        return_string += all_letters[l_index + direction]
    
    return return_string

ui_str = str(input("for encryption:"))
ui_int = int(input("you direction:"))

print(f"{ui_str}/{ui_int} -> {encrypt(ui_str, ui_int)}")