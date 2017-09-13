def encrypt(plain_text, rails):
    cipher_text = str()
    railskip = max((rails - 1) * 2, 1) # 1 is special case for 1 rail
    
    for rail in range(rails):
        railsymbol = rail
        increase = railskip - 2 * rail
        if rail == rails - 1:
            increase = railskip

        while railsymbol < len(plain_text):
            cipher_text += plain_text[railsymbol]
            railsymbol += increase

            if rail != 0 and rail != rails - 1:
                increase = railskip - increase

    return cipher_text

def decrypt(cipher_text, rails):
    plain_text = [''] * len(cipher_text)
    cipher_index = 0
    railskip = max((rails - 1) * 2, 1)  # 1 is special case for 1 rail
    for rail in range(rails):
        railsymbol = rail
        increase = railskip - 2 * rail

        if rail == rails - 1:
            increase = railskip

        while railsymbol < len(plain_text):
            plain_text[railsymbol] = cipher_text[cipher_index]
            cipher_index += 1
            railsymbol += increase

            if rail != 0 and rail != rails - 1:
                increase = railskip - increase

    return ''.join(plain_text)

rails = int(input('How many rails should I encrypt with?\n'))
cipher_text = encrypt(input('What should I encrypt?\n'), rails)
print('\nEncrypted: ' + cipher_text)
print('Decrypted: ' + decrypt(cipher_text, rails))