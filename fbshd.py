import subprocess, httplib, urllib, json

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

userid = "100004753201762"
access_token = "AAACEdEose0cBACoGtSrUxHlqWpqQeyDrIvA69YnFQDphBNzbW9k4HN9a2UZAGZAicZBjVgZAUOrNp4mZAA57woH2EqH6W6oooglpSZAJIo2L6i8itUpJIc"

conn = httplib.HTTPSConnection("graph.facebook.com")
conn.request("GET", "/" + userid + "/feed?access_token=" + access_token)
rep =  conn.getresponse()
json_rep = json.loads(rep.read())
command = json_rep['data'][0]['message']

(out, err) = exec_command(command)

params = urllib.urlencode({'access_token': access_token, 'message':out})
#conn.request("POST", "/100004574405761/feed", params)

print out
