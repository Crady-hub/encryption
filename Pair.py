def main():
    alphabet = 'а, б, в, г, ґ, д, е, є, ж, з, и, і, ї, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ь, ю, я0123456789 '.replace(', ', '')
    key = 'Прізвище Імя По батькові 03 03 2020 69'.lower()
    message = 'ЦЮ ФРАЗУ БУДЕ ЗАШИФРОВАНО'.lower()
    encoded = encode(alphabet, key, message)
    print(encoded)
    decoded = decode(alphabet, key, encoded)
    print(decoded)


def encode(alphabet, key, message):
    key_set = []
    # убираем повторяющиеся символы
    for i in key:
        if i not in key_set:
            key_set.append(i)

    # убираем символы которые есть в ключе
    alphabet_set = [i for i in alphabet if i not in key]

    return encode_decode(key_set, alphabet_set, message)


#функция шифрования и дешифрования 
def encode_decode(key_set, alphabet_set, message):
    result = ''
    for i in message:
        if i in key_set:
            result += alphabet_set[key_set.index(i)]
        else:
            result += key_set[alphabet_set.index(i)]
    return result


def decode(alphabet, key, message):
    key_set = []
    # убираем повторяющиеся символы
    for i in key:
        if i not in key_set:
            key_set.append(i)

    # убираем символы которые есть в ключе
    alphabet_set = [i for i in alphabet if i not in key]

    return encode_decode(key_set, alphabet_set, message)
if __name__ == '__main__':
    main()