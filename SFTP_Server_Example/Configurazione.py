import ConfigParser
import paramiko
import base64

''' Eccezione Di Errore Di Configurazione '''
class ErroreConfigurazione(Exception):
	pass

	

''' Classe Utente '''	
class Utente(object):
	self.anonymous = False
	self.hashPassword = None
	self.percorsoRoot = None
	self.chiaviAutorizzate = []

	
''' Classe Configurazione '''
class Configurazione(object):
	
	def __init__(self, pathFileConfigurazione):
		self.pathFileConfigurazione = pathFileConfigurazione
		self.carica()
	
	def carica(self):
		# Sezione (Parte Racchiusa Tra [] Con Sotto Gli Attributi) Nel File Di Configurazione
		sezioneConf = 'pysftpd'
		
		'''Legge Il File Di Configurazione Principale'''
		config = ConfigParser.RawConfigParser()
		if not config.read(self.pathFileConfigurazione):
			raise ErroreConfigurazione("Impossibile Caricare Il File Di Configurazione %r" % (self.pathFileConfigurazione))
			
		'''Legge Indirizzo Host/Porta'''
		host = config.get(sezioneConf, 'listen_host')
		port = config.get(sezioneConf, 'listen_port')
		self.indirizzo = (host, port)
		
		'''Carica Le Chiavi Host'''
		chiaviHost = []
		# Itero Le Possibili Opzioni Nella Sezione Di Configurazione Specificata
		for nomeOpzione in config.options(sezioneConf):
			if nomeOpzione != "host_key" and not nomeOpzione.startswith("host_key"):
				continue
			nomeFile = config.get(sezioneConf, nomeOpzione)
			try: # Se nomeFile = Percorso Specificato Nell'Opzione 'host_key.0' Ho Un File RSAKey
				# Recupero Da Un File Contenente Chiavi RSA La Chiave Host
				chiaveHost = paramiko.RSAKey.from_private_key_file(filename=nomeFile)
			except paramiko.SSHException: # Altrimenti Solleva Eccezione
				# Recupero Da Un File Contenente Chiavi DSS La Chiave Host ()
				chiaveHost = paramiko.DSSKey.from_private_key_file(filename=nomeFile)
			chiaviHost.append(chiaveHost)
			chiaveHost = None						# Elimino Referenza Alla Chiave
		if not chiaviHost:
			raise ErroreConfigurazione("Il File Di Configurazione %r Non Specifica Nessuna Chiave Host" % (self.pathFileConfigurazione))
		self.chiaviHost = chiaviHost
		
		'''Carica Il File Di Autenticazione Utente (authconfig.ini)'''
		configAutenticazione = ConfigParser.RawConfigParser()
		configAutenticazione.read(config.get(sezioneConf, 'auth_config'))
		utenti = {}
		# Gli Usernami Identificazione La Sezione Nel File Di Autenticazione Utente
		for username in auth_config.sections():
			user = User()
			# Se L'Utente Si Chiama Anonymous Setto L'Attributo A True
			if configAutenticazione.has_option(username, 'anonymous'):
				user.anonymous = configAutenticazione.getboolean(username, 'anonymous')
			# Se L'Attributo Non E' Settato Recupero La Password
			if not user.anonymous:
				user.hashPassword = configAutenticazione.get(username, 'password')
			# Recupero Il Percorso Principale
			user.percorsoRoot = configAutenticazione.get(username, 'root_path')
			
			user.chiaviAutorizzate = []
			if configAutenticazione.has_option(username, 'authorized_keys_file'):			
				nomeFile = configAutenticazione.read(username,'authorized_keys_file')
				for rawline in open(nomeFile,'r'):
					# Tolgo Spazi
					line = rawline.strip()
					if not line or line.startswith("#"):
						continue
					if line.startswith("ssh-rsa ") or line.starswith("ssh-dds "):
						# Ottengo Il Campo Della Chiave
						try:
							# Ottengo Una Tupla Separando Da Spazi Tutti Gli Spezzoni Della Chiave
							# Creo Uno Stringa Unendo Ogni Elemento Della Tupla Ad Un Separatore Di Spazio
							# Quindi Elimino Gli Spazi A Sinistra
							# E Splitto La Stringa In Base Agli Spazi Ottenendo Tupla Di Cui Prendo Primo Elemento
							campoChiave = " ".join(line.split(" ")[1:]).lstrip().split(" ")[0]
						except:
							continue
						if line.starswith("ssh-rsa"):
							# Ottengo Un Oggetto RSAKey
							chiave = paramiko.RSAKey(data=base64.decodestring(d))
						else:
							# Ottengo Un Oggetto DSSKey
							chiave = paramiko.DSSKey(data=base64.decodestring(d))
						del campoChiave
						user.chiaviAutorizzate.append(chiave)
			# Assegno NomeUtente => Oggetto Utente Nel Dizionario
			utenti[username] = utente
		self.utenti = utenti
	
	