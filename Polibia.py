def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyz .?!,+=-()'
    message = 'cogito, ergo sum'

    # создание квадрата 6х6
    square = [list(alphabet[i-6:i]) for i in range(6, len(alphabet)+1, 6)]

    encoded = encode(alphabet, message, square)
    print(encoded)
    decoded = decode(alphabet, encoded, square)
    print(decoded)

def encode(alphabet, message, square):
    # последовательность пар чисел 02221012312250420425102242303220
    step = ''.join([
        str(j)+str(square[j].index(i)) 
        for i in message 
        for j in range(len(square)) if i in square[j]
        ])

    # сдвиг на 3 символа влево 21012312250420425102242303220022
    step = step[3:] + step[0:3]

    #зашифрованное сообщение nbpirem +cqpdoao
    encode = ''.join([
        square[int(step[i])][int(step[i+1])] 
        for i in range(0, len(step), 2)
        ])
    return encode

def decode(alphabet, message, square):
    # последовательность пар чисел 21012312250420425102242303220022
    step = ''.join([
        str(j)+str(square[j].index(i)) 
        for i in message 
        for j in range(len(square)) if i in square[j]
        ])

    # сдвиг на 3 символа вправо 02221012312250420425102242303220
    step = step[-3:] + step[:-3]

    # расшифрованное сообщение cogito, ergo sum
    decode = ''.join([
        square[int(step[i])][int(step[i+1])] 
        for i in range(0, len(step), 2)
        ])
    return decode

if __name__ == '__main__': 
    main()