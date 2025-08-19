import string

all_letters = list(string.ascii_letters)
all_letters.extend(["ä", "ö", "ü", "Ä", "Ö", "Ü", " "])
all_letters.sort()
#print(all_letters)

running = True

def encrypt(this_string: str, direction: int) -> str:
    return_string = ""

#    idea of mapping certain letters out    
#    map = str.maketrans(" _", "_ ")
#    direction.trandlate(map)

    for letter in this_string:
        if letter in all_letters:
            l_index = all_letters.index(letter)
            return_string += all_letters[(l_index + direction) % len(all_letters)]
        else:
            return_string += letter
    return return_string

def decrypt(this_string:str, direction:int) -> str:
    return encrypt(this_string, direction*-1)

while running:
    ui_str = str(input("for encryption:"))
    ui_int = int(input("you direction:"))
    encrypted = encrypt(ui_str, ui_int)
    decrypted = decrypt(encrypted, ui_int)

    print(f"{ui_str}/{ui_int} -> {encrypted}")
    print(f"{encrypted}/{ui_int*-1} -> {decrypted}")
    
    yes_or_no = str(input("want to proceed? (yes/no)"))
    
    if yes_or_no.lower() == "no":
        running = False
        print("BYE!!")