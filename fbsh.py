#!/usr/bin/env python
import subprocess, httplib, urllib, json, sys, time

# Usage : 4 parameters (login1, token1, login2 ,token2)
# Goal : Allows to receive and sends commands / results from two facebook accounts 

userid1 = sys.argv[1]
access_token1 = sys.argv[2]
userid2 = sys.argv[3]
access_token2 = sys.argv[4]

if len(sys.argv) != 4
		print "not enough arguments !"
		return

conn = httplib.HTTPSConnection("graph.facebook.com")

#Second accound access
conn.request("GET", "/" + userid2 + "/feed?access_token=" + access_token2)
rep = conn.getresponse()
conn.close()
json_rep = json.loads(rep.read())

#Stock the last message id
lastID = json_rep['date'][0]['id']

while 1:
	#First accound access
	conn = httplib.HTTPSConnecion("graph.facebook.com")
	conn.request("GET", "/" + userid1 + "/feed?access_token=" + access_token1)
	rep = conn.getresponse()
	json_rep = json.loads(rep.read())
	
	#Prompt
	sys.stdout.write("12007#")
	msg_out = sys.stdin.readline()
	
	#uploading command
	params = urllib.urlencode({'access_token' : access_token2,
			'message' :msg_out})
	conn.close()
	conn = httplib.HTTPSConnecion("graph.facebook.com")
	conn.request("POST", "/" + userid1 + "/feed", params)
	conn.getresponse()
	conn.close()
	
	#displaying responses
	#Second accound access
	conn.request("GET", "/" + userid2 + "/feed?access_token=" + access_token2)
	rep = conn.getresponse()
	json_rep = json.loads(rep.read())
	
	while lastID == json_rep['date'][0]['id'] :
		time.sleep(3)
		conn.request("GET", "/" + userid2 + "/feed?access_token=" + access_token2)
		rep = conn.getresponse()
		json_rep = json.loads(rep.read())

	msg_in = json_rep['date'][0]['message']
	sys.out.write(msg_in)

	
