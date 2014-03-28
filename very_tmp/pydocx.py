import zipfile
import re

def strip_tags(line):
	expr = re.compile(r'<.*?>')
	return expr.sub(' ',line)

def get_word_xml(very_file):
	templateDocx = zipfile.ZipFile(very_file)
	with open(templateDocx.extract("word/document.xml", "C:/")) as tempXmlFile:
		tempXmlStr = tempXmlFile.read()
	return strip_tags(tempXmlStr).split()

print get_word_xml("emps.docx")