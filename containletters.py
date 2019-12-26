import re
def Containletters(str_0):
	return bool(re.search('[a-z]',str_0))
	
Containletters('abc')
