#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import hashlib
import random
import os

def main(args):
    return 0

if __name__ == '__main__':
		os.system("clear");
		print "\n\n" + \
		"_______________________________________________\n"+\
		"| Python | Reverse SSH Tunnelling |MkKonfig|###|\n"+\
		"|____  __|________________________|________|###|________________________________________________\n" +\
		"+##############9 ############  ##################################o  #################  \#xxxxxxx+\n"  +\
		"|####b        ##\ ##########  ##################################o o  ################  d##xxxxxx|\n"  +\
		"+####/ ######  ##9 ########  ###7            ###6  ####9  #####o  #o  #####/    #####  \###xxxxx+\n"  +\
		"|####b ##  \##  ##\ ######  ####3            ###8  ####8  ####o  ###o  ####b     ####  d####xxxx|\n"  +\
		"+####/ ##  d##  ###9 ####  #####7 ###7  ###  ###6  ####9  ###o  #####o  ###/  #   ###  \#####xxx+\n"  +\
		"|####b ######  #####\ ##  ###########3  ########8         ##o  #######o  ##b  ##   ##  d######xx|\n"  +\
		"+####/        #######9   ############7  ########6  ....   ##o  #######o  ##/  ###   #  \#######x+\n"  +\
		"|####b  ##############\ #############3  ########8  ####8  ###o  #####o  ###b  ####     d######xx|\n"  +\
		"+####/ ###############9 #############7  ########6  ####9  ####o  ###o  ####/  #####    \#####xxx+\n"  +\
		"|####b  ##############\ #############3  ########8  ####8  #####o  #o  #####b  ######   d####xxxx|\n"  +\
		"+####/ ###############9 #############7  ########6  ####9  ######o o  ######/  #######  \###xxxxx+\n"  +\
		"|####b  ##############\ #############3  ########8  ####8  #######o  #######b  ########  ##xxxxxx|\n"  +\
		"+####/  ##############9 #############7  #########  ####9  ########o########/  ######### ###xxxxx+\n"  +\
		"|####b ##############################3  ########## ####8  #################b  ##############xxxx|\n"  +\
		"+####/###############################7  ###############9  #################/  #############xxxxx+\n"  +\
		"|#########################################################################################xxxxxx|\n"  +\
		"+##########################################################################################xxxxx+\n"  +\
		"|#########################################################################################xxxxxx|\n\n"	
		print "[+] This script will generate a configuration file for the client."
		address_srv = raw_input("Insert bind address server \n(es: http://192.168.1.88/host.php):")
		address_ssh = raw_input("Insert bind address ssh:")
		port = raw_input("Insert bind port ssh:")
		clear_username = raw_input("Insert username or write generate to get one:")
		print "[+] Hashing the username with sha224..."
		username = hashlib.sha224(clear_username).hexdigest()
		clear_password = raw_input("Insert password or write generate to get one:")
		print "[+] Hashing the password with sha224..."
		password = hashlib.sha224(clear_password).hexdigest()
		arr_keys = ["Anon","Void","All","Network","Acid"]
		key = arr_keys[random.randint(0,4)]
		print "[+] Got key:%s" % key
		print "[+] Hashing the key with sha224..."
		key = hashlib.sha224(key).hexdigest()
		print "[+] All variables ready, making konfig.conf file"
		# Not Obfuscated
		'''
		file_b64 = base64.b64encode(
		"##############################################" +
		"[!]address_srv:%s#\n[!]address_ssh:%s#\n[!]port:%s#\n[!]username:%s#\n[!]password:%s#\n[!]key:%s#\n" % (address_srv,address_ssh,port,username,password,key) +
		"##############################################")
		'''
		# Obfuscated
		file_b64 = base64.b64encode(
		"##############################################" +
		"[!]h2893h4tgnw2hjjnppj09nnj:%s#\n[!]aaiosndoaisdoiqw9012u3040:%s#\n[!]ppslqkwiiickano3n4o1h0as:%s#\n[!]xjkiieolakeoowkansqwe123:%s#\n[!]ieeowlllakw123asw0006mmd:%s#\n[!]owiev0w9ejh0923jhr4iamso:%s#\n" % (address_srv,address_ssh,port,username,password,key) +
		"##############################################")
		Konfig = open("wertyuiopsdfghjkcvbn","w")
		Konfig.write(file_b64)
		print "[+] Client konfig file made"
		Konfig.close()
		print "[+] Writing server konfig file..."
		if not os.path.exists("%s//ServerKonfig.conf" % os.path.dirname(os.path.abspath(__file__))):
			server_file =  open("ServerKonfig.conf",'w')
			print "[+] No server konfig file found, made new one"
		else:
			server_file = open("ServerKonfig.conf", "a")
			print "[+] Server konfig file found, opened in append mode"
		server_file.write(
		"##############################################\n" +
		"[!]username:%s#\n[!]clear_text:%s#\n[!]password:%s#\n[!]clear_text:%s#\n" % (username, clear_username, password, clear_password) +
		"##############################################\n")
		print "[+] Server konfig file wrote, exiting..."
		server_file.close()
