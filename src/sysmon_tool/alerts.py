import json,urllib.request
def webhook(url,payload):
 body=json.dumps(payload).encode(); req=urllib.request.Request(url,data=body,headers={'Content-Type':'application/json'},method='POST')
 with urllib.request.urlopen(req,timeout=10) as r:return r.status
