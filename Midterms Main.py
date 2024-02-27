alphabet =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
userInput = input("Plaintext: ").upper()
shift = int(input("Shift Pattern: "))
output = ''
key = shift if shift < len(alphabet) else (len(alphabet) - shift)

for index in range(len(userInput)):
    placeholder = userInput[index]
    location = alphabet.find(placeholder)
    newLocation = location + key
    output += userInput[index] if location < 0 else alphabet[location]

print('Cipher Text is: %s' %(output))