from string import ascii_lowercase

def encode(string, shift):
    result = ""

    string = string.lower()
    for c in string:
        index_id = ascii_lowercase.index(c)
        new_index_id = (index_id + shift) % 26

        result += ascii_lowercase[new_index_id]
    
    return result

def decode(string, shift):
    result = ""

    string = string.lower()
    for c in string:
        index_id = ascii_lowercase.index(c)
        new_index_id = (index_id - shift) % 26
        
        result += ascii_lowercase[new_index_id]
    
    return result

def cipher_caesar(string, shift, type):
    result = ""

    string = string.lower()
    for letter_position in string:
        if letter_position not in ascii_lowercase:
            result += letter_position
            continue
        index_id = ascii_lowercase.index(letter_position)
        new_index_id = (index_id + shift * type) % 26
        result += ascii_lowercase[new_index_id]
    
    return result


def encode(string, shift):
    return cipher_caesar(string, shift, 1)

def decode(string, shift):
    return cipher_caesar(string, shift, -1)

if __name__ == '__main__':
    shift = None
    option = input("Encode(E) or Decode(D)?")

    if option == 'E' or 'e':
        try:
            enc = input("Key to be encrypted: ")
            print("Letter shifts: ")
            shift = int(input())
        
            print(f"Encrypted code= {encode(enc, shift)}")
        except EOFError:
            print("Invalid encode/shift input")
    elif option == 'D' or 'd':
        try:
            dec = input("Key to be decoded: ")
            print("Letter shifts: ")
            shift = int(input())

            print(f"Key decoded= {decode(dec, shift)}")
        except EOFError:
            print("Invalid encode/shift input")
    else:
        print("Invalid selection")
