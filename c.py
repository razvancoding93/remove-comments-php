import os

file = open('test.txt', 'r')
#print(file.read(2))

while 1:
	char = file.read(1)          # read by character
	if not char: break
	print(char),

file.close()

def compile(file):
	f= open("guru99.txt","w+")

# compile(file)


def create_directory(directory_name):
	# define the access rights
	access_rights = 0o755

	try:
		os.mkdir(directory_name, access_rights)
	except OSError:
		print ("Creation of the directory %s failed" % directory_name)
	else:
		print ("Successfully created the directory %s" % directory_name)
		
create_directory('test');

input("Press enter to exit ;)")