def split_len(seq, length): return [seq[i:i + length] for i in range(0, len(seq), length)] 
def decode( key , encrypted ):
    order = { int(val): num for num, val in enumerate(key) }
    plaintext = ''
    for column in range( len(encrypted) // len(key) ):
        for row in range(len(key)):
            plaintext += split_len(encrypted, len(encrypted) // len(key) )[ list( order.keys() )[ row ] - 1 ][ column ]
    return plaintext
print(decode('3214', 'LARPT HUONTSINCQCM NSOEIURAOITNE'))