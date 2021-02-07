def RunPy(package_name):
	if package_name == "":
		return "Error"
	if package_name == "Test":	
		import Test
		Test.run()