import json 
import subprocess

a = json.loads(open('valid.json').read().decode('utf-8'))
from pprint import pprint
# pprint(json.dumps(a["Dependencies"]))

b = str(json.dumps(a["Dependencies"]))

# print(len(a["Dependencies"]))

# count = len(a["Dependencies"])
# for x in range(0, count):
# 	print("Package %d" % (x))

def install(name):
	print(subprocess.call(['pip', 'install', name]))
	
for key, value in a["Dependencies"].items():
	
	mykeys = json.dumps(key)
	d = mykeys.replace('"', '')
	# print(d)
	try:
		install(d)
	except:
		print("Wrong URL")
		pass


file = open('a.txt','w')
file.write(b)
file.close()
