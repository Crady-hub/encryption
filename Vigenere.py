def main():
    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    sentence = 'I remember that September'.lower()
    key = 'leonid'
    encoded = encode(sentence, alphabet, key)
    print(f'Зашифрованное  сообщение:\n\'{encoded}\'')
    decoded = decode(encoded, alphabet, key)
    print(f'Расшифрованное сообщение:\n\'{decoded}\'')

def encode(sentence, alphabet, key):
    message = ''
    len_alphabet = len(alphabet)
    len_key = len(key)

    # индексы букв сообщения в алфавите
    sentence_num = [alphabet.index(i) for i in sentence]
    len_sentence = len(sentence_num)

    # индексы букв ключа в алфавите
    key_num = [alphabet.index(i) for i in key]

    # сумма идексов ключа и сообщения
    sum_key_sentence = [sentence_num[i]+key_num[i % len_key] for i in range(len_sentence)]

    # сумма индексов % длину алфавита
    encode = [i % len_alphabet for i in sum_key_sentence]

    for i in encode:
        message += alphabet[i]
    return message

def decode(encoded, alphabet, key):
    message = ''
    len_alphabet = len(alphabet)
    len_key = len(key)

    # индексы букв сообщения в алфавите
    sentence_num = [alphabet.index(i) for i in encoded]
    len_sentence = len(sentence_num)

    # индексы букв ключа в алфавите
    key_num = [alphabet.index(i) for i in key]

    # декодер
    decode_sentence = [(sentence_num[i] - key_num[i % len_key])% len_alphabet for i in range(len_sentence)]

    for i in decode_sentence:
        message += alphabet[i]
    return message

if __name__ == '__main__':
    main()
