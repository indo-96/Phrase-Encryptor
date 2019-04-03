#! /usr/bin/env python

"""
An encryptor that prompts for an input to either encrypt or decrypt - using a caesar-cipher
"""


def menu_list():
    # Display a menu upon startup
    print("\n**MENU**\n1. Encrypt String\n2. Decrypt String\n3. Brute Force Decryption\n4. Quit")
    return


def menu_choice():
    # Prompt user for input; gets the users choice
    x = input("\nWhat would you like to do? [1, 2, 3, 4]?\n:")
    return x


def encryption_choice():
    # Prompt user for a choice on what they want to encrypt;
    #       - input a string or a text file
    print("\nWhat do you want to encrypt:\n1. text file\n2. written input\n")
    y = input("Please enter either a '1 or 2'   :")
    return y


# ------ Entry Point ------
while True:
    # call function to display menu options
    menu_list()
    # get user choice
    menu_option = menu_choice()

    if menu_option < 1 or menu_option > 4:
        # Input error checking
        print("Please enter either a '1, 2, 3 or 4'.")
        menu_option = 0

    if menu_option == 1:
        # Encrypt with a key - caesar cipher
        encryption_option = encryption_choice()

        if encryption_option == 1:
            # User wants to encrypt a text file
            path = input("Please provide path to text file - surround path with "" : ")
            # std_array stores the contents of the text file
            # Dec_array stores the decimal value of each character for the text file
            # encr_array stores the new ASCII value of the encrypted text file
            offset = 0
            std_array = []
            Dec_array = []
            encr_array = []
            # open the text file
            f = open(path, 'r')

            if f.mode == 'r':
                contents = f.read()
                print("\n--- Original Text ---\n{} ".format(contents))  # Display the contents of the original text file

            for line in contents:
                std_array.append(line)

            # Prompt for user input for an offset value
            if offset < 1 or offset > 94:
                offset = input("Please enter an offset Key between (1 - 94) : ")

            # This for loop obtains the decimal value for each character
            for i in range(len(std_array)):
                Dec = ord(std_array[i])
                Dec_array.append(Dec)

            # This is the encryption for loop, uses the offset value to displace the decimal representation, which
            #   then converted back into a character - The encryption.
            for i in range(len(Dec_array)):
                value = 0
                if ord(std_array[i]) == 10:
                    # Skip the new line character - don't encrypt the new line to not mess with formatting.
                    encr_array.append("\n")
                    continue
                value = Dec_array[i] + offset
                if value > 126:
                    value = value - 95
                new_ASCII = value
                new_char = chr(new_ASCII)
                encr_array.append(new_char)
            # Make string out of the new array characters
            ES = ''.join(encr_array)
            print("\n--- Encrypted Text ---\n{} ".format(ES))
            # Write a new encrypted text file.
            f2 = open('encrypted_{}'.format(path), 'w')
            f2.write(ES)
            f2.close()
            print("\nSaved encrypted file under : 'encrypted_{}'".format(path))

        if encryption_option == 2:
            # User wants to input a string manually
            offset = 0
            # String prompt
            string_normal = raw_input("\nPlease enter a string to encrypt : ")
            string_normal = list(string_normal)
            string_dec = []
            encrypted_string = []
            # Offset value
            if offset < 1 or offset > 93:
                offset = input("Please enter an offset Key between (1 - 93) : ")

            # Getting the decimal values of the characters in the string
            for i in range(len(string_normal)):
                Dec = ord(string_normal[i])
                string_dec.append(Dec)

            # Encryption loop
            for i in range(len(string_normal)):
                value = 0
                value = string_dec[i] + offset
                if value > 126:
                    value = value - 95
                new_ASCII = value
                new_char = chr(new_ASCII)
                encrypted_string.append(new_char)
            # Join the array to display the encrypted string
            ES = ''.join(encrypted_string)
            print("\n--- Encrypted String ---\n{} ".format(ES))

    if menu_option == 2:
        # Decryption with a known key
        offset = 0
        decrypt_string = raw_input("\nPlease enter string to decrypt : ")
        decrypt_string = list(decrypt_string)
        decrypt_dec = []
        decrypted_string = []
        if offset < 1 or offset > 94:
            offset = input("Please enter decryption Key : ")

        for i in range(len(decrypt_string)):
            Dec = ord(decrypt_string[i])
            decrypt_dec.append(Dec)

        for i in range(len(decrypt_string)):
            value = 0
            value = decrypt_dec[i] - offset
            if value < 36:
                value = value + 95
                if value > 126:
                    value = value - 95
            actual_ASCII = value
            actual_char = chr(actual_ASCII)
            decrypted_string.append(actual_char)

        AS = ''.join(decrypted_string)
        print("\n--- Decrypted String ---\n{} ".format(AS))

    if menu_option == 3:
        # Decrypt with a brute force attack
        offset = 1
        print("Using a brute force attack")
        decrypt_string = raw_input("\nPlease enter string to decrypt : ")
        decrypt_string = list(decrypt_string)
        decrypt_dec = []
        decrypt_length = len(decrypt_string)

        for i in range(decrypt_length):
            Dec = ord(decrypt_string[i])
            decrypt_dec.append(Dec)

        while offset < 95:
            decrypted_string = []
            for j in range(decrypt_length):
                value = 0
                value = decrypt_dec[j] - offset
                if value < 36:
                    value = value + 95
                    if value > 126:
                        value = value - 95
                actual_ASCII = value
                actual_char = chr(actual_ASCII)
                decrypted_string.append(actual_char)

            AS = ''.join(decrypted_string)
            print("Offset {} : {}".format(offset, AS))
            offset += 1

    if menu_option == 4:
        exit()
