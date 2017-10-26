def cipher(message, shift):
    result = str()
    for character in message:
        new_ordinal = ord(character) + shift
        result += chr(new_ordinal)
    
    print(f"Your translated text is {result}")

# 1 is encrypt, 2 is decrypt
mode = int(input("Should I encrypt (1) or decrypt (2)? "))

# Make sure that our shift offset is within range.
shift = int(input("What is the shift offset? ")) % 26
message = input("What is the message? ")

if mode == 1:
    cipher(message, shift)
elif mode == 2:
    # We multiply shift by -1 since we want to subtract the shift.
    cipher(message, shift * -1)
else:
    print("Invalid mode input. Try again.")

