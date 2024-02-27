import math

def split_len(seq, length): return [seq[i:i + length] for i in range(0, len(seq), length)] 

def decode( key , encrypted ):
    order = { int(val): num for num, val in enumerate(key) }

    plaintext = ''

    col = math.ceil(len(encrypted) / len(key))

    for column in range( col ):
        for row in range(len(key)):
            try: plaintext += split_len(encrypted, col )[ list( order.keys() )[ row ] - 1 ][ column ] 
            except IndexError: continue
    return plaintext

print(decode('3214', 'lwde lhorlo'))
