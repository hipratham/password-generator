import random
# difining all  the characters to use in the password
numbers = "0123456789"
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%&+=-/?()[]{}"

allcharacters = list(numbers + lowercase + uppercase + symbols)
password_length = int(input("Enter the password length that you want:  "))

while True:
    password = ''.join(random.choice(allcharacters) for i in range (password_length))
    print("Generated password:", password)
    a = input("If you want next type 'redo' else type 'ok':  ")
    if a == "redo":
        continue  
    else:
        print("Process complete")
        break  
