host = '10.10.129.142'
port = '14000'

command = 'curl -i "http://%s:%s/webhdfs/v1/?op=GETHOMEDIRECTORY"' % (host, port)
import  os

os.system(command)