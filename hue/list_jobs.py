import urllib2
import json
import ast

status_api = 'http://10.10.129.141:11000/oozie/v1/job/%s'
trigger_api = 'http://10.10.129.141:11000/oozie/v1/jobs?action=start'

req = urllib2.Request('http://10.10.129.142:8888/oozie/editor/workflow/list/')
response = urllib2.urlopen(req)
output = response.read()

print output

mydict = json.loads(output) #json.dumps(json.loads(output), indent=4, separators=(',', ': '))




