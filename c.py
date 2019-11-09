import os
import re
from shutil import copy

def _replacer(match):
	if match.group(2) is not None:
		return ""
	else:
		return match.group(1)

def remove_comments_from_file_regex(filepath):
	f = open(filepath, 'r', encoding="utf-8", errors='ignore')
	content = f.read()
	pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"
	regex  = re.compile(pattern, re.MULTILINE|re.DOTALL)

	content = regex.sub(_replacer, content)

	f.close()
	return content

def compile(filepath):
	filepath_compiled = filepath.replace( '\project', '\compiled')
	os.makedirs(os.path.dirname(filepath_compiled), exist_ok=True)

	if filepath.endswith('.php'):
		content = remove_comments_from_file_regex(filepath)
		f = open(filepath_compiled, "w+", encoding="utf-8", errors='ignore')
		f.write(content)
		f.close()
	else:
		copy(filepath, filepath_compiled)

def processEachFile(directory):

	for subdir, dirs, files in os.walk(directory):
		for filename in files:
			filepath = subdir + os.sep + filename
			compile(filepath)

processEachFile(r'.\project')

input("Press enter to exit ;)")
