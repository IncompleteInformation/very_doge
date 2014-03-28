#!C:/python27/python.exe
import cgi
import cgitb; cgitb.enable()
import os, sys
import zipfile
import re
from pyth.plugins.rtf15.reader import Rtf15Reader
from pyth.plugins.plaintext.writer import PlaintextWriter
import msvcrt
import subprocess
msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
msvcrt.setmode (1, os.O_BINARY) # stdout = 1

UPLOAD_DIR = os.getcwd() + "\\.." + "\\very_tmp"
HTML_TEMPLATE = """<!DOCTYPE HTML>
<html><head><title>very doge</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<form action="%(SCRIPT_NAME)s" method="POST" enctype="multipart/form-data">
<input name="file_1" type="file"><br>
<input name="submit" type="submit">
<img src= "http://96.42.106.210/{0}" alt="such incompatible">

</form>
</body>
</html>"""
SIMPLE_TEMPLATE = """<!DOCTYPE html>
<html>
{0}
</html>"""
def print_html_form (filename):
  null_filename = False
  if filename == "":
    filename = "choose_file.jpg"
    null_filename = True
    """This prints out the html form. Note that the action is set to
      the name of the script which makes this is a self-posting form.
      In other words, this cgi both displays a form and processes it.
    """
  print "content-type: text/html\n"
  if null_filename:
    print HTML_TEMPLATE.format(filename) % {'SCRIPT_NAME':os.environ['SCRIPT_NAME']}
  else:
    filename=filename[71:]
    #filename=filename[77:]
    filename = filename.replace("\\","/")
    print HTML_TEMPLATE.format(filename) % {'SCRIPT_NAME':os.environ['SCRIPT_NAME']}

def save_uploaded_file (form_field, upload_dir):
    """This saves a file uploaded by an HTML form.
       The form_field is the name of the file input field from the form.
       For example, the following form_field would be "file_1":
           <input name="file_1" type="file">
       The upload_dir is the directory where the file will be written.
       If no file was uploaded or if the field does not exist then
       this does nothing.
    """
    form = cgi.FieldStorage()
    if not form.has_key(form_field): return
    fileitem = form[form_field]
    if not fileitem.file: return
    x = fileitem.filename
    if x == "":
      return
    tmp_filename = os.path.join(upload_dir, fileitem.filename)
    fout = file (tmp_filename, 'wb')
    while 1:
        chunk = fileitem.file.read(100000)
        if not chunk: break
        fout.write (chunk)
    fout.close()
    return tmp_filename
###########################DOGECODE#####################################
#import sys
#import os

import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import random
import collections


wow_pardir = os.path.join(os.getcwd(), os.pardir)
much_picture = os.path.join(wow_pardir, "dogepic.jpg")
so_ignore = open(os.path.join(wow_pardir, "ignore-large.php"))
plz_ignore = so_ignore.read().split()
plz_srs_ignore = set()

for very_stuff in plz_ignore:
  plz_srs_ignore.add(very_stuff.upper())
meny_words = 10
so_first = ["SUCH","SO","VERY","MUCH","MANY"]
much_muzzle = [533,270]
such_radius = 110
srs_face = [420,180]
srs_size = 214

def strip_tags(line):
  expr = re.compile(r'<.*?>')
  return expr.sub(' ',line)

def get_word_xml(very_file):
  templateDocx = zipfile.ZipFile(very_file)
  with open(templateDocx.extract("word/document.xml", "C:/")) as tempXmlFile:
    tempXmlStr = tempXmlFile.read()
  return strip_tags(tempXmlStr).split()

def get_rtf(very_file):
  rtf = Rtf15Reader.read(open(very_file))
  return PlaintextWriter.write(rtf).getvalue().split()

def srs_get_pdf(very_file):
  txtname = very_file[:-4]+".txt"
  subprocess.call(["C:\\Program Files\\Xpdf\\bin32\\pdftotext.exe", very_file])
  #subprocess.call(["C:\\Program Files (x86)\\Xpdf\\bin32\\pdftotext.exe", very_file])
  f = open(txtname)
  return f.read().split()

def srs_get_doc(very_file):
  txtname = very_file[:-4]+".txt"
  subprocess.call(["C:\\Program Files\\Convert Doc\\ConvertDoc.exe", "/S", very_file, "/T", txtname, "/F9 /C1 /M2"])
  #subprocess.call(["C:\\Program Files (x86)\\Convert Doc\\ConvertDoc.exe", "/S", very_file, "/T", txtname, "/F9 /C1 /M2"])
  f = open(txtname)
  return f.read().split()


def wow():
  so_filename = save_uploaded_file("file_1", os.path.join(os.getcwd(), os.pardir, "very_tmp"))
  if so_filename == None:
    print_html_form("")
    return
  elif so_filename.endswith(".docx"):
    such_words = get_word_xml(so_filename)
  elif so_filename.endswith(".doc"):
    such_words = srs_get_doc(so_filename)
  elif so_filename.endswith(".rtf"):
    such_words = get_rtf(so_filename)
  elif so_filename.endswith(".pdf"):
    such_words = srs_get_pdf(so_filename)
  elif so_filename.endswith(".html") or so_filename.endswith(".htm"):
    wow_file = open(so_filename)
    such_words = wow_file.read()
    strip_tags(such_words)
    such_words = such_words.split()
  else:
    wow_file = open(so_filename)
    such_words = wow_file.read().split()
  very_dict = collections.defaultdict(int)
  such_words = filter(lambda so_amaze: so_amaze.upper() not in plz_srs_ignore, such_words)
  such_words = filter(lambda so_amaze: so_amaze.isalpha(), such_words)
  for very_word in range(len(such_words)):
    if such_words[very_word].upper() in very_dict:
      very_dict[such_words[very_word].upper()] += 1
    else:
      very_dict[such_words[very_word].upper()] = 1

  return very_dict, len(such_words), so_filename

def such_picture(so_dict):
  if so_dict == None:
    return
  much_name = so_dict[2] + ".jpg"
  such_long = float(so_dict[1])
  very_coordinates = [[srs_size, srs_size, srs_face[0], srs_face[1]]]
  so_dict = so_dict[0]
  such_image = Image.open(much_picture)
  many_pixel = such_image.size
  many_pixel = list(many_pixel)
  much_count = 0.0
  meny_bad = 0

  for so_entry in sorted(so_dict, key=so_dict.get, reverse=True):
    much_count += so_dict[so_entry]
    #print SIMPLE_TEMPLATE.format(so_entry)
    if meny_bad > meny_words:
      break
    meny_bad+=1

  meny_bad = 0 #such again, so amaze. wow.
  such_average = 0
  for so_entry in sorted(so_dict, key=so_dict.get, reverse=True):
    if meny_bad > meny_words:
      break
    such_heavy = float(so_dict[so_entry])
    so_size = int(round(many_pixel[0]*such_heavy/much_count/2))
    such_average+=so_size
    such_hold = such_text(such_image, so_entry, so_size, many_pixel, very_coordinates)
    such_image = such_hold[0]
    very_coordinates = such_hold[1]
    meny_bad += 1
  such_average /= meny_words
  such_text(such_image,"WOW", such_average, many_pixel, very_coordinates)
  so_smart_such_save(such_image, much_name)

def so_smart_such_save(very_image, much_name):
  very_image.save(much_name)
  print_html_form (much_name)

def such_similar(wow_color, wow_other_color):
  such_total = 0
  such_threshold = 80
  for so_counting in range(3):
    such_total += abs(wow_color[so_counting]-wow_other_color[so_counting])
  if such_total < such_threshold:
    return True
  else:
    return False

def such_text(wow_image, so_text, very_size, such_pixels, many_collision):

  very_random = random.randint(0,len(so_first)-1)
  if os.name == 'nt':
    very_font = ImageFont.truetype("C:\\Windows\\Fonts\\Comic.ttf", very_size)
  if os.name == 'posix':
    very_font = ImageFont.truetype("/Library/Fonts/Comic Sans MS.ttf", very_size)
  so_draw = ImageDraw.Draw(wow_image)
  very_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
  while such_similar(very_color, [0xCC,0xCC,0x99]):
    very_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
  if so_text!="WOW":
    wow_word = so_first[very_random] + " " + so_text
  else:
    wow_word = so_text
  such_big = so_draw.textsize(wow_word, very_font)
  while such_big[0] >= wow_image.size[1]:
    very_size -= 1
    if os.name == 'nt':
      very_font = ImageFont.truetype("C:\\Windows\\Fonts\\Comic.ttf", very_size)
    if os.name == 'posix':
      very_font = ImageFont.truetype("/Library/Fonts/Comic Sans MS.ttf", very_size)
    such_big = so_draw.textsize(wow_word, very_font)
  such_x = random.randint(0,such_pixels[0]-such_big[0])
  so_y = random.randint(0,such_pixels[1]-such_big[1])

  such_crowded = True
  such_tired = 500
  while such_crowded:

    if such_tired == 0:
      break

    wow_happy = True
    for so_collision in many_collision:
      if much_bump([such_big[0], such_big[1], such_x, so_y], so_collision):
        wow_happy = False
    
    if wow_happy:
      such_crowded = False
      break

    such_x = random.randint(0,such_pixels[0]-such_big[0])
    so_y = random.randint(0,such_pixels[1]-such_big[1])
    such_tired-=1

  so_draw.text((such_x, so_y-int(such_big[1]/2.0)), wow_word, font=very_font, fill=very_color)
  so_draw = ImageDraw.Draw(wow_image)
  many_collision.append([such_big[0], such_big[1], such_x, so_y])

  return wow_image, many_collision

def much_bump(very_try, very_stay):
  #0=width,1=height,2=x,3=y
  such_ghandi = 5
  very_try_center = [very_try[0]/2.0+very_try[2], very_try[1]/2.0+very_try[3]]
  very_stay_center = [very_stay[0]/2.0+very_stay[2], very_stay[1]/2.0+very_stay[3]]
  such_okay = 2

  if abs(very_try_center[0]-very_stay_center[0]) < very_try[0]/2.0 + very_stay[0]/2.0:
    such_okay -= 1

  if abs(very_try_center[1]-very_stay_center[1]) < very_try[1]/2.0 + very_stay[1]/2.0:
    such_okay -= 1

  if such_okay > 0:
    return False
  else:
    return True




##########################/DOGECODE#####################################
such_picture(wow())