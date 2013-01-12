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

userid = sys.argv[1]
access_token = sys.argv[2]

#key = b'lablanquetteestbonnebienbonneoui'
#iv = Random.new().read(AES.block_size)
#cipher = AES.new(key, AES.MODE_CFB, iv)

if len(sys.argv) != 3:
  print "not enough arguments !"
	sys.exit()


#Second account access
conn = httplib.HTTPSConnection("graph.facebook.com")
conn.request("GET", "/" + userid + "/feed?access_token=" + access_token)
rep = conn.getresponse()
json_rep = json.loads(rep.read())

#Stock the last message id
dataLength = len(json_rep['data'])
cpt_f = 0
cpt_t = 0

	
#uploading command
conn.close()
for i in range(dataLength):
	ID = json_rep['data'][i]['id']
	conn = httplib.HTTPSConnection("graph.facebook.com")
	print ID
	conn.request("DELETE", "/" + ID)
	reponse =  json.loads(conn.getresponse().read())
	print str(reponse)
	if reponse == "true":
		cpt_t = cpt_t + 1
	else:
		cpt_f = cpt_f + 1
	conn.close()

print "true : " + str(cpt_t) + " false : " + str(cpt_f)



	
