import sys
import os
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import random
import collections

such_picture = "dogepic.jpg"
so_ignore = open("ignore-large.php")
plz_ignore = so_ignore.read().split()
plz_srs_ignore = set()
for very_stuff in plz_ignore:
	plz_srs_ignore.add(very_stuff.upper())
meny_words = 15
so_first = ["SUCH","SO","VERY","MUCH","MANY"]
much_muzzle = [533,270]
such_radius = 110
#srs_face = [540,288]
such_factor = 1
srs_face = [420*such_factor,180*such_factor]
srs_size = 214*such_factor

def wow():
	wow_file = open("e_proc")
	if len(sys.argv) > 1:
		wow_file = open(sys.argv[1])
	else:
		print "such mistake, more filename"

	such_words = wow_file.read().split()

	very_dict = collections.defaultdict(int)
	#for much_word in plz_ignore:
	such_words = filter(lambda so_amaze: so_amaze.upper() not in plz_srs_ignore, such_words)
	such_words = filter(lambda so_amaze: so_amaze.isalpha(), such_words)
	for very_word in range(len(such_words)):
		if such_words[very_word].upper() in very_dict:
			very_dict[such_words[very_word].upper()] += 1
		else:
			very_dict[such_words[very_word].upper()] = 1

	return very_dict, len(such_words)

def wow_such_old():

	if len(sys.argv) > 1:
		f = open(sys.argv[1])
	else:
		print "such mistake, more filename"

	such_words = f.read().split()
	for very_word in range(len(such_words)):
		such_temp = such_words[very_word]
		if not such_temp[0].isalpha():
			such_temp=such_temp[1:]
		if len(such_temp) > 0:
			if not such_temp[-1].isalpha():
				such_temp=such_temp[:-1]
		such_words[very_word] = such_temp

	very_dict = {}
	very_dict["wow"] = 1
	for many in range(len(such_words)):
		if such_words[many].upper() == "WOW":
				very_dict["wow"] += 1
		if (such_words[many]).upper() in so_first:
			many_word = such_words[many]+" "+such_words[many+1]

			if many_word in very_dict:
				very_dict[many_word] += 1
			else:
				very_dict[many_word] = 1
	return very_dict

def such_picture(so_dict):
	such_long = float(so_dict[1])
	very_coordinates = [[srs_size, srs_size, srs_face[0], srs_face[1]]]
	so_dict = so_dict[0]
	such_picture = "dogepic.jpg"
	such_image = Image.open(such_picture)
	many_pixel = such_image.size
	many_pixel = list(many_pixel)
	if not such_factor==1:
		many_pixel[0] = many_pixel[0]*such_factor
		many_pixel[1] = many_pixel[1]*such_factor
		such_image = such_image.resize((many_pixel[0], many_pixel[1]), Image.ANTIALIAS)


  	meny_bad = 0
  	much_count = 0.0
 	for so_entry in sorted(so_dict, key=so_dict.get, reverse=True):
 		much_count += so_dict[so_entry]
		if meny_bad > meny_words:
			break
		meny_bad+=1

	meny_bad = 0 #such again, so amaze. wow.
	for so_entry in sorted(so_dict, key=so_dict.get, reverse=True):
		if meny_bad > meny_words:
			break

		such_heavy = float(so_dict[so_entry])

		so_size = int(round(many_pixel[0]*such_heavy/much_count/2))
		such_hold = such_text(such_image, so_entry, so_size, many_pixel, very_coordinates)
		such_image = such_hold[0]
		very_coordinates = such_hold[1]
		meny_bad += 1
	
	#such_image = wow_many_box(such_image, very_coordinates)
	if not such_factor == 1:
		many_pixel[0] = many_pixel[0]/such_factor
		many_pixel[1] = many_pixel[1]/such_factor
		such_image = such_image.resize((many_pixel[0], many_pixel[1]), Image.ANTIALIAS)
	so_smart_such_save(such_image)

def wow_many_box(wow_picture, such_datas):
	for much_box in such_datas:
		so_draw = ImageDraw.Draw(wow_picture)
		so_draw.rectangle([much_box[2],much_box[3],much_box[0]+much_box[2],much_box[1]+much_box[3]], fill=None)
		so_draw = ImageDraw.Draw(wow_picture)

	so_draw.rectangle([0,0,1130,692])
	so_draw = ImageDraw.Draw(wow_picture)
	return wow_picture

def so_smart_such_save(very_image):
	such_files = []
	wow_directory = os.getcwd()
	wow_directory += "/such_made"

	many_want = "{0}{1}{2}".format("very_", sys.argv[1], "_000.jpg")

	for such_file in os.listdir(wow_directory):
		such_files.append(such_file)

	so_counting = 1
	while many_want in such_files:
		many_want = many_want[:-7]
		many_want = "{0}{1}{2}".format(many_want, "%03d" %so_counting, ".jpg")
		so_counting += 1

	much_name = wow_directory + "/" + many_want
	very_image.save(much_name)

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
	very_font = ImageFont.truetype("/Library/Fonts/Comic Sans MS.ttf", very_size)
	so_draw = ImageDraw.Draw(wow_image)
	very_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
	while such_similar(very_color, [0xCC,0xCC,0x99]):
		very_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
	wow_word = so_first[very_random] + " " + so_text
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

	if such_crowded:
		print "wow. {0} such hard to fit".format(wow_word)

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

def such_test():
	wow_directory = os.getcwd()
	wow_directory += "/such_made"
	for such_file in os.listdir(wow_directory):
		print such_file

such_picture(wow())