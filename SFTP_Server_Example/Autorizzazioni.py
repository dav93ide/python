import paramiko
import crypt

class Autorizzazioni(paramiko.ServerInterface):
	
	utenti = None
	
	def __init__(self, utenti, setFunzioneAutenticazioneUtente):
		self.utenti = utenti
		self._setUserAutenticato = setFunzioneAutenticazioneUtente
		
	def getAutenticazioniPermesse(self, username):
		return "publickey,password"
		
	# Controlla Esistenza Del Nome Utente Tra Quelli Recuperati Dal File
	def checkAutenticazione(self, username):
		if username == 'anonymous' or username in self.utenti or self.utenti[username].anonymous:
			self._setUserAutenticato(self.utenti[username])
			return paramiko.AUTH_SUCCESSFUL
		else:
			return paramiko.AUTH_FAILED
	
	# Controllo Se La Password E' Corretta
	def checkPasswordAutenticazione(self, username, password):
		if username == 'anonymous' and username in self.users and self.users[username].anonymous:
			# 'anonymous' Può Usare Qualunque Password
			pass
		# Se Username In Lista Utenti
		elif username in self.utenti:
			passwordHash = self.users[username].hashPassword
			if crypt.crypt(password, passwordHash) != passwordHash:
				return paramiko.AUTH_FAILED
		else:
			return paramiko.AUTH_FAILED
		self._setUserAutenticato(self.users[username])
		return paramiko.AUTH_SUCCESSFUL
	
	# Controllo Se La Chiave Pubblica E' Corretta
	def checkAutenticazionePublicKey(self, username, chiave):
		if username == 'anonymous' and username in self.users and self.users[username].anonymous:
            # 'anonymous' Può Usare Qualunque Chiave Pubblica
            pass
		elif username in self.utenti:
			if chiave not in self.utenti[username].chiaviAutorizzate:
				return paramiko.AUTH_FAILED
		else:
			return paramiko.AUTH_FAILED
		self._setUserAutenticato(self.users[username])
		return paramiko.AUTH_SUCCESSFUL
		
	# Controllo Richiesta Canale
	def checkRichiestaCanale(self, tipo, idCanale):
		if tipo == 'session':
			return paramiko.OPEN_SUCCEEDED
		return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
			