import string

all_letters = list(string.ascii_letters)
all_letters.extend(["ä", "ö", "ü", "Ä", "Ö", "Ü", " "])
all_letters.sort()

print(all_letters)

def encrypt(this_string: str, direction: int) -> str:
    return_string = ""

#    idea of mapping certain letters out    
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

def decrypt(this_string:str, direction:int) -> str:
    return encrypt(this_string, direction*-1)

ui_str = str(input("for encryption:"))
ui_int = int(input("you direction:"))
encrypted = encrypt(ui_str, ui_int)
decrypted = decrypt(encrypted, ui_int)

print(f"{ui_str}/{ui_int} -> {encrypted}")
print(f"{encrypted}/{ui_int*-1} -> {decrypted}")