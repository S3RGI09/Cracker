#!/usr/bin/python3


import hashlib


print()
print("  ____ ____      _    ____ _  _______ ____  ")
print(" / ___|  _ \    / \  / ___| |/ / ____|  _ \ ")
print("| |   | |_) |  / _ \| |   | ' /|  _| | |_) |")
print("| |___|  _ <  / ___ \ |___| . \| |___|  _ < ")
print(" \____|_| \_\/_/   \_\____|_|\_\_____|_| \_\   V1.5")
print()
print("creado por S3RGI09 (Sergio Casero Verdial)")

encontrada = 0
print("-----------------------------------------------")
input_hash = input("Inserte la contraseña hasheada: ")
pass_doc = input("Inserte el diccionario: ")
print("-----------------------------------------------")

try:
	pass_file = open(pass_doc, 'r')
except:
	print("Error:" + pass_doc + "no ha sido encontrada")

for palabra in pass_file:
	palabra_cifrada = palabra.encode('utf-8')
	palabra_haseada = hashlib.md5(palabra_cifrada.strip())
	digest = palabra_haseada.hexdigest()

	if digest == input_hash:
		print("contraseña encontrada!!! \n La contraseña es: " + palabra)
		encontrada = 1
		break

if not encontrada:
	print("Contraseña no encontrada en el archivo " + pass_doc)
