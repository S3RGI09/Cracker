#!/usr/bin/python3


import hashlib


print()
print("  ____ ____      _    ____ _  _______ ____  ")
print(" / ___|  _ \    / \  / ___| |/ / ____|  _ \ ")
print("| |   | |_) |  / _ \| |   | ' /|  _| | |_) |   github.com/S3RGI09")
print("| |___|  _ <  / ___ \ |___| . \| |___|  _ < ")
print(" \____|_| \_\/_/   \_\____|_|\_\_____|_| \_\   V1.5")
print()
print("\033[;36m"+"Creado por S3RGI09 (Sergio Casero Verdial)")

encontrada = 0
print("\033[1;31m"+"--------------------------------------------")
input_hash = input("\033[1;32m"+"[+] Inserte la contraseña haseada MD5: "+'\033[0;m') 
pass_doc = input("\033[1;32m"+"[+] Inserte el diccionario: "+'\033[0;m') 
print("\033[1;31m"+"--------------------------------------------")

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
