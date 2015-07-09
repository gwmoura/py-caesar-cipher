from caesar_cipher import *

phrase = "George is smart"
result = encrypt(phrase)

print('ROT-0')
print(result)
print(decrypt(result))

for n in range(0,25):
	result = encrypt(phrase, n)
	print('')
	print('ROT-'+str(n))
	print(result)
	print(decrypt(result,n))