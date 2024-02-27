def split_len(seq, length): return [seq[i:i + length] for i in range(0, len(seq), length)] 

def encode( key , plaintext ):
    order = { int(val): num for num, val in enumerate(key) }

    cipherText = ''

    for index in sorted (order.keys()):
        for part in split_len(plaintext, len(key)): 
            try: cipherText += part[order[index]]
            except IndexError:
                continue
    return cipherText

originalText = input('Enter Text: ').upper()

numberOfKeys = int(input("Enter number of keys or columns: "))

key = input("Enter key sequence: ")

while(numberOfKeys != len(key)):
    key = input(f"Enter {numberOfKeys} key sequence: ")
    
print("Encrypted text: " + encode(key, originalText))