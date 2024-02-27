code = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

userInput = input("Enter a string: ")

output = ''

def decrypt(userInput, output, code):

    for index in range(len(userInput)):
        temporary = userInput[index]
        location = code.find(temporary)
        newLocation = location - 3
        output += code[newLocation]
    print(output)

decrypt(userInput.upper(), output, code)