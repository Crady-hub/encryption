def main(message, key):
    print(f'Сообщение для шифрования: {message}\nКлюч: {key}')
    sorted_key = sorted(key) 

    key_int = num_key(key, sorted_key)
    encoded = encode(message, key_int) 
    decoded = decode(encoded, key_int).replace('*','')
    
    return f'Зашифрованное сообщение: \'{encoded}\'\nРасшифрованное сообщение: \'{decoded}\'\n'

def encode(message, key_int):
    line = []
    lines = []
    encoded = []
    len_key_int = len(key_int)

    # заполняем возможные пустые ячейки 
    while len(message) % len_key_int != 0:
        message += '*'

    # создаем массивы длиной в ключ
    for i in range(len(message)):
        line.append(message[i])
        if len_key_int == len(line):
            lines.append(line)
            line = []
    
    # делаем транспонированние и меняем столбцы по сортированному ключу
    for i in range(len_key_int):
        for j in range(len(lines)):
            encoded.append(lines[j][key_int.index(i)])
    return ''.join(encoded)

def decode(message, key_int):
    line = []
    lines = []
    transpose = []
    decoded = []
    len_key_int = len(key_int)
    # количество строк
    row = int(len(message)/ len_key_int)
    
    # создаем массивы длиной в ключ
    for i in range(len(message)):
        line.append(message[i])
        if row == len(line):
            lines.append(line)
            line = []

    # делаем транспонированние 
    for i in range(row):
        for j in range(len(lines)):
            line.append(lines[j][i])
            if len(line) == len_key_int:
                transpose.append(line)
                line = []

    # меняем столбцы по несортированному ключу
    for i in range(len(transpose)):
        for j in key_int:
            decoded.append(transpose[i][j])
    return ''.join(decoded)

def num_key(key, sorted_key): # индексы ключа по алфавиту [4, 0, 2, 3, 1] == virus
    key_int = []
    for i in range(len(key)):
        for j in range(len(sorted_key)):
            if key[i] == sorted_key[j]:
                sorted_key[j] = '*'
                key_int.append(j)
                break
    return key_int

if __name__ == '__main__':
    print('TEST 1')
    print(main(message = 'we are discovered flee at once', key ='virus'))
    print('TEST 2')
    print(main(message = 'we are discovered', key = 'book'))
    print('TEST 3')
    print(main(message = 'we are discovered flee at once flee at once', key = 'hello'))