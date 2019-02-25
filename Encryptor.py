"""
An encryptor that prompts for an input to either encrypt or decrypt - using a caesar-cipher
"""


def menu_list():
    print("\n**MENU**\n1. Encrypt String\n2. Decrypt String\n3. Brute Force Decryption\n4. Quit")
    return


def menu_choice():
    x = input("\nWhat would you like to do? [1, 2, 3, 4]?\n:")
    return x


while True:
    menu_list()
    menu_option = menu_choice()

    if menu_option < 1 or menu_option > 4:
        print("Please enter either a '1, 2, 3 or 4'.")
        menu_option = 0

    if menu_option == 1:
        # Encrypt with a key
        offset = 0
        string_normal = raw_input("\nPlease enter a string to encrypt : ")
        string_normal = list(string_normal)
        string_dec = []
        encrypted_string = []
        if offset < 1 or offset > 94:
            offset = input("Please enter an offset Key between (1 - 94) : ")

        string_length = len(string_normal)

        for i in range(string_length):
            Dec = ord(string_normal[i])
            string_dec.append(Dec)

        for i in range(string_length):
            value = 0
            value = string_dec[i] + offset
            if value > 126:
                value = value - 95
            new_ASCII = value
            new_char = chr(new_ASCII)
            encrypted_string.append(new_char)

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

        decrypt_length = len(decrypt_string)

        for i in range(decrypt_length):
            Dec = ord(decrypt_string[i])
            decrypt_dec.append(Dec)

        for i in range(decrypt_length):
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

        while offset < 94:
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
