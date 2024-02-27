import math

def split_len(seq, length): return [seq[i:i + length] for i in range(0, len(seq), length)] 

def encode( key , plaintext ,numberOfKeys ):
    order = { int(val): num for num, val in enumerate(key) }

    cipherText = ''

    col = math.ceil(len(plaintext) / numberOfKeys )

    for row in range (numberOfKeys):
        for column in range (col):
            try: cipherText += split_len(plaintext, numberOfKeys )[ column ][ list( order.keys() )[ row ] - 1 ]
            except IndexError: continue
    return cipherText

originalText = input('Enter Text: ').upper()

numberOfKeys = int(input("Enter number of keys or columns: "))

key = input("Enter key sequence: ")

while(numberOfKeys != len(key)):
    key = input(f"Enter {numberOfKeys} key sequence: ")

print("Encrypted text: " + encode(key, originalText, numberOfKeys))