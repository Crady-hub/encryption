def main(text, key):
    encoded = ''.join(encode(text, key))
    print(f'Зашифрованное сообщение: \"{encoded}\"')
    print('Зашифрованное сообщение utf-8: ', encoded.encode('utf-8'))
    decoded = ''.join(decode(key, encoded))
    print('Расшифрованние сообщение:',decoded)
    
def encode(text, key):
    # в двоичную систему счисления 
    bin_text = [bin(c)[2:].rjust(8, '0') for c in text.encode('utf-8')]
    bin_key = [bin(c)[2:].rjust(8, '0') for c in key.encode('utf-8')]
    len_text = len(bin_text)
    len_key = len(bin_key)

    # ascii ['\x05', '\x1c', 'L', "'", '\n', 'X']
    xor = [chr(int(bin_text[i], 2)^int(bin_key[i%len_key], 2)) for i in range(len_text)]
    return xor

def decode(key, encoded):
    # в двоичную систему счисления
    bin_text = [bin(c)[2:].rjust(8, '0') for c in encoded.encode('utf-8')]
    bin_key = [bin(c)[2:].rjust(8, '0') for c in key.encode('utf-8')]
    len_text = len(bin_text)
    len_key = len(bin_key)

    # ascii ['H', 'e', 'l', 'l', 'o', '!']
    xor = [chr(int(bin_text[i], 2)^int(bin_key[i%len_key], 2)) for i in range(len_text)]
    return xor

if __name__ == '__main__':
    print('TEST 1')
    main(text = 'Hello!', key = 'My Key')
    print('TEST 2')
    main(text = 'Hello World!', key = 'Word')
    print('TEST 3')
    main(text = 'Hi!', key = 'Wool')