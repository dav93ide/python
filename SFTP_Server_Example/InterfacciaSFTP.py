import paramiko
import os
import stat
import posixpath
import sys

class InterfacciaSFTP(paramiko.SFTPServerInterface):
	
	def __init__(self, server, funzioneGetUtente):
		self._directoryBase = funzioneGetUtente().percorsoRoot
		
	''' Ritorna Il Percorso Locale Passando Un Percorso SFTP '''
	def _pathLocale(self, pathSftp):
		if sys.platform == 'win32':
			# Bisogna Controllare Caratteri Non Ammessi
		percorsoAssolutoBase = os.path.abspath(self._directoryBase)
		if not pathSftp.startswith("/"):
			raise ValueError("Percorso FSTP Invalido %r" % percorsoAssolutoBase)
		percorso = posixpath.normpath(pathSftp)
		percorso = percorso.lstrip("/")
		assert('..' not in posixpath.split(percorso) )
		lpercorso = os.path.abspath(os.path.join(self._directoryBase, percorso))
		assert(os.path.commonprefix( (percorsoAssolutoBase, lpercorso) ) == percorsoAssolutoBase)
		return lpercorso
	
	# Ritorna Tupla Di Oggetti SFTPAttributes Creati Usando L'Oggetto Ottenuto Da os.stat Eseguito Sui Vari File
	def list_folder(self, pathSftp):
		pathLocale = self._pathLocale(pathSftp)
		returnVal = []
		# Per Ogni File Nel Percorso Aggiungo A Tupla Oggetto SFTPAttributes Con Info
		for filename in os.listdir(pathLocale):
			localPathFile = os.path.join(pathLocale, filename)
			returnVal.append(paramiko.SFTPAttributes.from_stat(os.lstat(localPathFile), filename))
		return returnVal
	
	# Ritorno Oggetto SFTPAttributes Creato Usando L'Oggetto Ottenuto Da os.stat
	def stat(self, pathSftp):
		pathLocale = self._pathLocale(pathSftp)
		filename = os.path.basename(pathLocale)
		return paramiko.SFTPAttributs.from_stat(os.stat(pathLocale), filename)
	
	def lstat(self, pathSftp):
		pathLocale = self._pathLocale(pathSftp)
		filename = os.path.basename(pathLocale)
		return paramiko.SFTPAttributs.from_stat(os.lstat(pathLocale), filename)
	
	# Apre Un File Sul Server E Crea Una Maniglia Per Future Operazioni Su Esso
	def open(self, pathSftp, flags, attributi):
		pathLocale = self._pathLocale(pathSftp)
		if (flags & os.O_WRONLY) or (flags & os.O_RDWR ):
			return paramiko.SFTP_PERMISSION_DENIED
		handle = paramiko.SFTPHandle()
		handle.readfile = open(pathLocale, 'rb')
		return handle
			