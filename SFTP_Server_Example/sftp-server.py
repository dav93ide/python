import optparse
import sys
import os
import logging
import pwd
import grp
import paramiko
from sftpd.CLI import CLI

if __name__ == '__main__':
    CLI().main()