alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cifred = "DEFGHIJKLMNOPQRSTUVWXYZABC"

def decrypt(phrase):
	new_prhase = ''
	for letter in list(phrase.upper()):
		pos = cifred.find(letter)
		if pos != -1:
			new_prhase+=alphabet[pos]
		else:
			new_prhase+=letter

	return new_prhase


def encrypt(phrase):
	new_prhase = ''
	for letter in list(phrase.upper()):
		pos = alphabet.find(letter)
		if pos != -1:
			new_prhase+=cifred[pos]
		else:
			new_prhase+=letter

	return new_prhase


