import subprocess
import os
path = os.path.join(os.getcwd(), os.pardir, "very_tmp", "blood.pdf")
print path
formatted = "pdftotext \"{0}\"".format(path)
print formatted
os.system(formatted)