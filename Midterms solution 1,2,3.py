# Solution 1

userInput = input("Plaintext: ").upper()

key = int(input("Shift Pattern: "))

alphabet =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

output = ''

def caesar(userInput, alphabet, key, output):
    for index in range(len(userInput)):
        placeholder = userInput[index]
        location = alphabet.find(placeholder)
        newLocation = location + key

        if len(userInput) < key:
            newLocation -= key  

            if(newLocation > 0):
                output += alphabet[newLocation]
            else:
                output += " "
        else:
            if(newLocation > 0):
                output += alphabet[newLocation]
            
            else:
                output += " "
            
    print('Cipher Text is: %s' %(output))

caesar(userInput, alphabet, key, output)

# Solution 2

userInput = input("Plaintext: ").upper()

key = int(input("Shift Pattern: "))

alphabet =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

output = ''

def caesar(userInput, alphabet, key, output):

    for index in range(len(alphabet)):

        for character in userInput:

            if character in alphabet:
                newIndex = alphabet.find(character)
                newIndex = newIndex + index
            
                if newIndex <  0:
                    newIndex = newIndex + len(alphabet)
                
                output += alphabet[newIndex]

            else:
                output += character


    print('Cipher Text is: %s' %(output))


caesar(userInput, alphabet, key, output)

# Solution 3

alpha =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
userInput = input("Plain Text: ").upper()
key = int(input("Shift Pattern: "))
output = ""

for i in range( len(userInput) ):
    c = userInput[i]
    loc = alpha.find(c)
    newloc = loc + key

    if(userInput[loc] == " "):
        output += ' '
        print("dpsce")
    else:
        output += alpha[newloc]


print ('Cipher Text:', output)