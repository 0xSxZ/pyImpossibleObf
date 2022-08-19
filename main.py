import os

def transcrireCle(cle):
	return "".join([str(ord(elt)) for elt in cle])

def deobfuscate(arg):
	message = ""
	cle = transcrireCle("0xSxZ")
	chiffre = arg
	for i in range(len(chiffre)):
		chiffre[i] -= int(cle[i % len(cle)])
		message += chr(chiffre[i])
	return message

def obfuscate(msg):
	if(os.path.isfile(msg)):
		print("[.] Obfuscating : " + msg)
		cle = transcrireCle("0xSxZ")
		chiffre = []
		message = open(msg).read()

		for elt in message:
			chiffre.append(ord(elt))


		for i in range(len(chiffre)):
			pos_cle = i % len(cle)
			chiffre[i] += int(cle[pos_cle])
		crypt = ""
		for elt in chiffre:
			try:
				crypt += chr(elt)
			except UnicodeEncodeError:
				crypt += "x"
		open(msg + ".hashed.py", "x").write("import hashy\nexec(hashy.deobfuscate("+ str(chiffre) + "))")
		print("[.] Successfully obfuscated : " + msg)
		return chiffre
	else:
		print("[.] Please input a valid path.")