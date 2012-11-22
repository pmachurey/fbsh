#All rights reserved - Tvalli

import httplib, urllib

params = urllib.urlencode({'access_token': 'AAACEdEose0cBAMRxnEDN8VwoUzZAARgFsoHNjA2UzfevZAMeLKYUOA6tV2nQ0RGe3ZCOjwW1JOLCpBo9w2ZBPEM1FuD9Qru2sqJEWqPZAugOuEgxARUWO'})
conn = httplib.HTTPConnection("graph.facebook.com")
conn.request("GET", "/100004574405761/feed", params)
rep =  conn.getresponse()
print rep.status, rep.reason
print rep.read()
