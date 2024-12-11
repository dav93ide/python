import SocketServer
from InterfacciaSFTP import InterfacciaSFTP
from Autorizzazioni import Autorizzazioni
from errori import ErroreProtocollo
import paramiko

class ServerSFTP(SocketServer.TCPServer):			# Eredito Da Un Server TCP
	
	def __init__(self, indirizzoServer, Configurazione, ClasseGestoreRichiesta=None):
		# Se Gestore Non Fissato Setto Un Gestore Di Richiesta Connessione  Di Base
		if ClasseGestioneRichiesta is None:
			ClasseGestoreRichiesta = GestoreRichiestaConnessione
		# Inizializzo La Superclasse
		SocketServer.TCPServer.__init__(self, indirizzoServer, ClasseGestoreRichiesta)
		
		# Attributi A Cui Accede ClasseGestoreRichiesta
		self.users = configurazione.users					# Recupero Utenti
		self.host_keys = configurazione.host_keys			# Recupero Chiavi Hosts

		
class SFTPConnectionRequestHandler(SocketServer.BaseRequestHandler)			# Eredito Da Gestore Base Di Richiesta
	
	timeoutAutenticazione = 120				# Timeout Dell'Autenticazione
	
	# Setup Della Classe
	def setup(self):
		self.trasporto = self.creaTrasporto(self.request)		# Ottento Un Oggetto transport Da Paramiko
		self.loadModuliServer()
		self.setOpzioniSicurezza()
		self.addChiaviHost()
		self.setGestoriSottosistema()
	
	def handle(self):
		# Creo Un Interfaccia Per Autorizzazioni Passando Lista Utenti E Funzione Di Autenticazione
		interfacciaSrv = Autorizzazioni(self.server.users, self._setUtenteAutenticato)
		self.trasporto.start_server(server=interfacciaSrv)		# Negozia Sessione SSH2 Come Server
		# Ottiene Canale Di Sessione
		canale = self.trasporto.accept(self.timeoutAutenticazione)	# Ottiene Il Canale Aperto Dal Client
		if canale is None:
			raise ErroreProtocollo('Canale Di Sessione Non Aperto (Autenticazione Fallita?)')
		self.trasporto.join()				# Thread join
		
	# Funzione Di Autenticazione, Setta Un Utente Autenticato
	def _setUtenteAutenticato(self, utente):
		self._userAutenticato = utente
	
	def _getUtenteAutenticato(self):
		return self._userAutenticato
		
	# Ottiene Un Oggetto Transport, Crea Una Sessione SSH Attraverso La Socket
	def creaTrasporto(self, socket):
		return paramiko.Transport(socket)
	
	# Carica Un File Di Moduli Per Gruppo-Scambio Negoziazione 	Della Chiave (Usa Metodo Di Paramiko.Transport)
	def loadModuliServer(self):
		self.trasporto.load_server_moduli()			
	
	def setOpzioniSicurezza(self):
		# Ottiene Un Oggetto SecurityOptions Utilizzato Per Gli Algoritmi Di Encrypting Permessi
		opzioniSicurezza = self.trasporto.get_security_options()
		
		# Setta Algoritmi Digest
		# Non Supporta -> (hmac-sha1-96, hmac-md5, hmac-md5-96, none)
		opzioniSicurezza.digests = ('hmac-sha1',)
		
		# Supporta Compressione 'zlib' Rallentata, Ma Non Compressione 'zlib'
		# 'zlib@openssh.com' Fa La Stessa Cosa Di 'zlib', Ma Evita Attacchi Da Utenti Non Autenticati
		opzioniSicurezza.compression = ('zlib@openssh.com', 'none')
		
	def addChiaviHost(self):
		# Aggiung Chiavi Utilizzate Per La Modalità Server, Precedentemente Recuperate Dall'Oggetto Configurazione
		for chiave in self.server.host_keys:
			self.trasporto.add_server_key(chiave)
		
	def setGestoriSottosistema()
		# Setta La Classe Gestore Per Un Sottosistema In Modalità Server
		# ( nome, gestore , *larg, **kwarg )		Dove:
		# gestore = Sotto Classe Di SubsystemHandler
		# *larg = Oggetto Server Per La Sessione Che Ha Iniziato Questo Sottosistema ( Di Tipo ServerInterface)
		# **kwarg = Funzione Usata Nel Costruttore Dell'Interfaccia
		self.trasporto.set_subsystem_handler('sftp', paramiko.SFTPServer, sftp_si = InterfacciaSFTP, getUserFunc = self._getUtenteAutenticato)












