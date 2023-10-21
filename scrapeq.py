# scrape quotes from internet site goodreads.com
# adapted code from quote module which further uses gazpacho
# gazpacho parses html file from the website
# iq.py is a wrapper around it

import iq
import os

def scrape_quotes (num):
	tags = ["love", "life", "humour", "inspirational", "wisdom", "philosophy", "god", "truth", "poetry", "romance", "death", "happiness", "hope", "faith", "writing", "religion", "motivational", "relationship", "success", "spirituality", "time", "knowledge", "science"]
	
	path = os.getcwd()
	tag_dir = path + "/tags"

	if os.path.isdir(tag_dir) == False:
		os.mkdir(tag_dir)

	for tag in tags:
		print("Getting quotes for:", tag)
		qs = iq.iq (tag, "", limit=num)
		
		if qs != None:
		
			tag_file = tag_dir + "/" + tag + ".txt"
			print("Opening and writing to:", tag_file)
			f = open(tag_file, "w")
			f.write(str(qs))
			f.close()
			

