import os

file = open('test.txt', 'r')
chars = ''
previous_char = ''
comment_opened = False

while 1:
	# read file char by char and break at end
	char = file.read(1)
	if not char: break

	# detect comment
	if previous_char + char == '/*':
		comment_opened = True
		chars = chars[:-1]
	elif previous_char + char == '*/':
		comment_opened = False

	# if comment not detected add content to file
	if comment_opened == False and previous_char + char != '*/':
		chars += char

	previous_char = char

	# if previous_char + char == '*/':
	# 	chars = chars[:-1]
print(chars)

file.close()

def compile(content):
	f = open("guru99.txt","w+")
	f.write(content)
	f.close()

# compile(file)


def create_directory(directory_name):
	# define the access rights
	access_rights = 0o755

	if(os.path.isdir('./' + directory_name) != True):
		try:
			os.mkdir(directory_name, access_rights)
		except OSError:
			print ("Creation of the directory %s failed" % directory_name)
		else:
			print ("Successfully created the directory %s" % directory_name)
		
create_directory('test')

input("Press enter to exit ;)")