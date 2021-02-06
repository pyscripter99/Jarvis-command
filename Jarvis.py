import os
modules = {}
f = open(input()).readlines()
def run(txtin):
	args= txtin.split()
	command = args[0]
	args.remove(command)
	if command == "say":
		I = 1
		out = ""
		for x in range(len(args)):
			out = str(out) + " " + str(args[x])
		print(out)
	if command == "clear":
		os.system("clear")
	if command == "import":
		modules[args[0]] = open(args[0])
	if command == "wait":
		import time
		time.sleep(int(args[0]))
	if command == "run":
		g = modules[args[0]].readlines()
		for y in g:
			run(y)
for t in f:
	run(t)