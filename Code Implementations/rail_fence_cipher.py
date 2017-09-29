def encrypt(plain_text, rails):
    cipher_text = str()
    cycle = max((rails - 1) * 2, 1) # 1 is special case for 1 rail
    
    for rail in range(rails):
        ptr = rail
        character_distance = cycle - 2 * rail
        
        # Both the bottom and top rails have a (same) character distance of the cycle. 
        if rail == rails - 1:
            character_distance = cycle

        # While we have *something* to write
        while ptr < len(plain_text):
            cipher_text += plain_text[ptr]
            ptr += character_distance

            # If this is not the top or bottom rail, alternate between two distance patterns 
            # (one for going up a cycle and one for going down a cycle). 
            if rail != 0 and rail != rails - 1:
                character_distance = cycle - character_distance

    return cipher_text

def decrypt(cipher_text, rails):
    plain_text = [''] * len(cipher_text)
    cipher_index = 0
    cycle = max((rails - 1) * 2, 1)  # 1 is special case for 1 rail

    for rail in range(rails):
        ptr = rail
        character_distance = cycle - 2 * rail

        if rail == rails - 1:
            character_distance = cycle

        while ptr < len(plain_text):
            plain_text[ptr] = cipher_text[cipher_index]
            cipher_index += 1
            
            ptr += character_distance

            if rail != 0 and rail != rails - 1:
                character_distance = cycle - character_distance

    return ''.join(plain_text)

rails = int(input('How many rails should I encrypt with?\n'))
cipher_text = encrypt(input('What should I encrypt?\n'), rails)
print('\nEncrypted: ' + cipher_text)
print('Decrypted: ' + decrypt(cipher_text, rails))