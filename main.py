def do_add(self, s):
	l = s.split()
	if len(l) != 2:
		print("*** invalid number of arguments")
		return
	try:
		l = [int(i) for i in l]
	except ValueError:
		print("*** arguments should be numbers")
		return
	print(l[0]+l[1])