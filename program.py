# -*- coding: utf-8 -*-
from caesar_cipher import *

print("O que você deseja fazer?")
print("1 - Criptografar uma frase")
print("2 - Descriptografar uma frase")
option = int(raw_input(""))

if(option==1):
	phrase = raw_input("Qual sua frase para criptografar? ")
	print(encrypt(phrase, 25))
elif(option==2):
	phrase = raw_input("Qual sua frase para descriptografar? ")
	print(decrypt(phrase, 25))