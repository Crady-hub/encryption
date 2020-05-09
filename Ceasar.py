def ceasar():
	alphabet = "абвгдежзийклмнопрстуфхцчшщьыъдэюя "
	message = "активно шифруем"
	res = ''
	back = ''
	for i in message:
		res += alphabet[(alphabet.index(i) + 16) % len(alphabet)] 
	print(f'Зашифрованное сообщение: \'{res}\'')
	for i in res:
		back += alphabet[(alphabet.index(i) - 16 + len(alphabet)) % len(alphabet)]
	print(f'Расшифрованное сообщение: \'{back}\'')

if __name__ == '__main__':
	ceasar()

