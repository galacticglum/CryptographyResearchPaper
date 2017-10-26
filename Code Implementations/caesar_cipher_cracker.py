def cipher(message, shift):
    result = str()
    for character in message:
        new_ordinal = ord(character) + shift
        result += chr(new_ordinal)
    
    print(f"Your translated text is {result}")

def solve(message, max_key):
    # Start at the shift offset of 1
    for i in range(1, max_key):
        cipher(message, -i)

message = input("What do you want to solve? ")
max_key = int(input("What is the max key? "))
solve(message, max_key)