alpha =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str_in = input("Enter message, like HELLO: ").upper()
key = int(input("Shift Pattern: "))
n = len(str_in)
str_out = ""
for i in range(n):

    if str_in[i] == " ":
        str_out += " "

    else:
        c = str_in[i]
        loc = alpha.find(c)

        if key > n:
            newloc = loc - key
            str_out += alpha[newloc]

print ('Obfuscated version:', str_out)