import os
import Jarvis_connect
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
	if command == "connect":
		file_ = open("Jarvis_connect.py", "a")
		file_.write('\n' + "	if package_name == " + '"' + args[0] + '"' + ":" + "	" + '\n' + "		import " + args[0] + '\n' + "		" + args[0] + ".run()")
		file_.close()
	if command == "python":
		Jarvis_connect.RunPy(args[0])
for t in f:
	run(t)