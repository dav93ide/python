import optparse
import sys
import os
import logging
import pwd
import grp
import paramiko
from ServerSFTP import ServerSFTP
from Configurazione import Configurazione

class CLI(object):
	
	# Scorre Gli Argomenti
	def parse_args(self):
		# Default
		defaults = []
		defaults['config'] = "/etc/pysftpd/pysftpd.ini"
		
		# Scorri Opzioni
		op = optparse.OptionParser(usage="Usage: %s [opts]")
		op.add_option("-c", "--config", metavar = "FILE", dest="config", default=defaults['config'], help= "Carica Una Configurazione Del Programma Da FILE (default: %s)" % (defaults['config']))
		op.add_option("--user", metavar="NAME", dest="user", help = "setuid A Questo Utente Prima Di Accettare Connessioni ")
		op.add_option("--group", metavar="NAME", dest="group", help = "setgid A Questo Gruppo Prima Di Accettare Connessioni")
		op.add_option("--chroot", metavar="PATH", dest="chroot", help ="[sperimentale] chroot Al PATH Prima Di Accettare Connessioni (Richiede --user E --group; Non Dimenticare Di Chiudere Descrittori Di File Aperti)")
		op.add_option("-v","--verbose", metavar="FILE", dest="verbosity", action="count", default=0, help = "Operazione 'Verbosa' (Permesse Opzioni '-v' Multiple)")
		
		(options,args) = op.parse_args()
		if len(args) != 0:
			print >> sys.stderr, "%s Errore: Argomenti Non Validi" % (sys.argv[0])
			sys.exit(1)
		if options.chroot and (not options.user or not options.group ):
			print >> sys.stderr, "%s Errore: --chroot Richiede --user E --group" % (sys.argv[0])
			sys.exit(1)
		return options
		
	def main(self):
		options = self.parse_args()
		
		# Log Verbosa
		if options.verbosity == 0:
            logging.basicConfig(level=logging.ERROR)
        elif options.verbosity == 1:
            logging.basicConfig(level=logging.INFO)
        elif options.verbosity >= 2:
            logging.basicConfig(level=logging.DEBUG)
		
		# Creo Oggetto Configurazione
		config = Configurazione(options.config)
		
		# Creo Oggetto ServerSFTP Passando Indirizzo E Oggetto Configurazione
		server = ServerSFTP(config.indirizzo, config = config)
		
		if options.chroot:
			uid = pwd.getpwnam(options.user)[2]
            gid = grp.getgrnam(options.group)[2]

            os.chroot(options.chroot)
            os.setgroups([])   	 						# Aggiunge Privilegi Supplementari Del Gruppo
            os.setgid(gid)
            os.setuid(uid)
		
		server.serv_forever()
		
		
		