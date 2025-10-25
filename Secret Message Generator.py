## encode
def encode():
    msg = input("Enter your message: ")
    key = int(input("Enter your shift key: "))
    new_msg =""

    for x in msg:
        if ord(x) >= 65 and ord(x) <= 90:           # checking if the character is in uppercase or not
            num = key + ord(x)
            if num > 90:                            # handling wrapping around for uppercase
                num = 65 + (num % 91)               
                new_msg += chr(num)
            else:
                new_msg += chr(num)
        elif ord(x) >= 97 and ord(x) <= 122:        # checking if the character is in lowercase or not
            num = key + ord(x)
            if num > 122:                           # handling wrapping around for lowercase
                num = 97 + (num % 123)
                new_msg += chr(num)
            else:
                new_msg += chr(num)
        else:
            new_msg += x
    print("Your encoded messages is:",new_msg)
    print()


# decode
def decode():
    msg = input("Enter your encoded message: ")
    key = int(input("Enter your shift key: "))
    new_msg =""

    for x in msg:
        if ord(x) >= 65 and ord(x) <= 90:           # Checking if the character is uppercase or not
            num = ord(x) - key
            if num < 65:                            # handling wrapping around for uppercase
                num = 91 -( 65-num)
                new_msg += chr(num)
            else:
                new_msg += chr(num)
        elif ord(x) >= 97 and ord(x) <= 122:        # checking if the character is in lowercase or not
            num = ord(x) - key
            if num < 97:                            # handling wrapping around for lowercase
                num = 123 - (97-num)
                new_msg += chr(num)
            else:
                new_msg += chr(num)
        else:
            new_msg += x
    print("Your decoded messages is:",new_msg)
    print()


# main function
def main():
    print(":::::::::: MENU ::::::::::")
    print("1: Encode a message")
    print("2: Decode a message")
    print("3: Exit")
    n = int(input("Enter your choice: "))
    match n:
        case 1:
            encode()
            main()
        case 2:
            decode()
            main()
        case 3:
            exit

main()