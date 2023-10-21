# get quotes from scraped quote database
# assumes scraping of quotes was done before and tags directory is populated with quotes by topic
# 
# this file provides 2 functions
# 1) get_topics - provides list of topics which are available with quotes
# 2) get_quote - get a random quote from a defined topic
# 3) get_random_quote - get a random quote from any topic

import random
import os

def get_topics():
	tag_dir = "./tags"
	topics = []
	topics.append("any")
	if os.path.isdir(tag_dir):
		tag_list = list(os.scandir(tag_dir))
		for item in tag_list:
			topics.append (item.name.rstrip(".txt"))
		return topics
	
def get_quote(tag):
	dir_path = os.getcwd()
	tag_dir = "/tags"
	if tag == "any":
		return get_quote_random_topic()
	else:
		tag_file = dir_path + tag_dir + "/" + tag + ".txt"
		f = open(tag_file)
		res = list(eval(f.read()))

		n = random.randint(0, (len(res) - 1))
		return (res[n].get("quote") + " -- " + res[n].get("author") + " -- " + res[n].get("book"))

def get_quote_random_topic ():

        # how to get random quote from any topic
        topics = get_topics()
        n = random.randint (0, len(topics))
        if n > 1:
        	return (get_quote(topics[n - 1]))
        else:
        	return (get_quote(topics[n]))

