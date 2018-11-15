def poly(*args):

	"""
	f(x) = a * x + b * x**2 + x**3 + ...
	*args = (x, a, b)
	"""
	if len(args) == 1:
		raise Exception("You have only entered a value for x and no coefficients.")
	
	x = args[0] # X value 
	#a = args[1]
	#b = args[2]
	
	coef = args[1:] 
	# convert to a loop
	result = 0
	for power, c in enumerate(coef):
		result += c * (x ** (power + 1))
	
	return result
	
	#print(args)
	
	#fx = a * x + b * (x ** 2)
	#return fx