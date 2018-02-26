import json 
import pip

a = json.loads(open('valid.json').read().decode('utf-8'))
from pprint import pprint
pprint(json.dumps(a["Dependencies"]))

b = str(json.dumps(a["Dependencies"]))

print(len(a["Dependencies"]))

# count = len(a["Dependencies"])
# for x in range(0, count):
# 	print("Package %d" % (x))


def install(package):
	pip.main(['install', package])

for key, value in a["Dependencies"].items():
	# print(key, value)
	# print(json.dumps(key))

	mykeys = json.dumps(key)
	d = mykeys.replace('"', '')
	# print(d)
	if __name__ == '__main__':
		install(d)

file = open('a.txt','w')
file.write(b)
file.close()
