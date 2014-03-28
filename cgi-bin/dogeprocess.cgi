#!C:/python27/python.exe
import cgi
import cgitb; cgitb.enable()
import os, sys


HTML_TEMPLATE = """<!DOCTYPE HTML>
<html>
<head>
<title>File Doge</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
</head><body><h1>{0}</h1>
<form action="%(SCRIPT_NAME)s" method="POST" enctype="multipart/form-data">
</form>
</body>
</html>"""

def print_html_form (stuff):
    print "content-type: text/html\n"
    print HTML_TEMPLATE.format(stuff) % {'SCRIPT_NAME':os.environ['SCRIPT_NAME']}



def break_everything():
	import subprocess
	import os
	path = os.path.join(os.getcwd(), os.pardir, "very_tmp", "blood.pdf")
	#path = "96.42.106.210/blood.pdf"
	#formatted = "pdftotext \"{0}\"".format(path)
	#subprocess.call(formatted)
	subprocess.call(["C:\\Program Files (x86)\\Convert Doc\\ConvertDoc.exe", "/S", "C:\\Program Files (x86)\\Apache Software Foundation\\Apache2.2\\htdocs\\very_doge\\very_tmp\\dost.doc", "/T", "C:\\Program Files (x86)\\Apache Software Foundation\\Apache2.2\\htdocs\\very_doge\\very_tmp\\dost.txt", "/F9 /C1 /M2"])
	#os.system("C:\\Program Files (x86)\\Apache Software Foundation\\Apache2.2\\htdocs\\very_doge\\such_doc.bat \"C:\\Program Files (x86)\\Apache Software Foundation\\Apache2.2\\htdocs\\very_doge\\very_tmp\\dost.doc\"")
	#subprocess.call(['vim','lol'])

	print_html_form(os.environ['COMSPEC'])

#print_html_form ()
break_everything()
