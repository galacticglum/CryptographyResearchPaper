import math

def handle_rail_iteration(on_iteration_function, width, rail_num):
    y = 0
    direction = 0
    for i in range(width):
        on_iteration_function(y, i)
        if y == 0:
            direction = 1
        elif y == rail_num - 1:
            direction = -1
            
        y += direction

def encrypt(plain_text, rail_num):
    width = len(plain_text)
    rows = [''] * rail_num

    def iteration(y, i):
        rows[y] += plain_text[i]

    handle_rail_iteration(iteration, width, rail_num)
    return ''.join(rows)
     
def decrypt(cipher_text, rail_num):
    width = len(cipher_text)
    rail_fence = [[] for i in range(rail_num)]
    handle_rail_iteration(lambda y, i: rail_fence[y].append(i), width, rail_num)

    ptr = 0
    decrypted = [''] * width

    for i in range(rail_num):
        for j in range(len(rail_fence[i])):
            decrypted[rail_fence[i][j]] = cipher_text[ptr]
            ptr += 1

    return ''.join(decrypted)

key = int(input('How many rails should I encrypt with? '))
plain_text = input('What should I encrypt? ')

result = encrypt(plain_text, key)
chunk_size = 5

print('\nEncrypted message: '+' '.join([result[i:i+chunk_size] for i in range(0, len(plain_text), chunk_size)]))
print('Decrypted message: ' + decrypt(result, key))