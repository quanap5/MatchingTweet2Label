#===================================================================================
#This scrip file to read json file for Earthquake project
#Editor: Nguyen Van Quan
#Date edit: 2016 Nov 08
#====================================================================================

#=================
# Libraries 
#=================
import re, os
import json
import csv
import time
import string


file_in='out.json'
file_out = os.path.splitext(file_in)[0]
# 2 output in scv format
out1 = open('FromJsontoRaw%s.csv'%(file_out), 'wb')
#out_time1 = open('FromJsontoRawKODUNG%sinterval%s.csv'%(file_out,interval_), 'w')

# create the csv writer object
#csv_time1 = csv.writer(out_time1)
#csv_time1.writerow(['Unix epoch','date','occurences%s'%interval_])

attribute=['id','created_at','lang','geo','text']
#csv.writerow(attribute)


t0=0;
inter_count=0;
m_count=1;

print ("Read Json of Tweets -----> CSV file")
with open(file_in, 'r') as f:
    	tweet_count = 0
	with out1 as f1:
		csv = csv.writer(f1, quoting=csv.QUOTE_ALL)
		csv.writerow(attribute)
	 
		for line in f:
			if 'created_at' in line and '"lang":"en"' in line:
				tweet = json.loads(line) # load it as Python dict
				#print(tweet) # pretty-print
				tweet_count += 1
				row = (
			    	tweet['id_str'],                    # tweet_id
			    	tweet['created_at'],            # tweet_time
		 		#tweet['timestamp_ms'],		# time Unix
			    	#tweet['user']['screen_name'],   # tweet_author
			    	#tweet['user']['id_str'],        # tweet_authod_id
			   	tweet['lang'],                  # tweet_language
			    	tweet['geo'],                   # tweet_geo
			    	tweet['text']                   # tweet_text
		       		)
		
				values = [(value.encode('utf8') if hasattr(value, 'encode') else value) for value in row]
				#values = [value for value in row]
				print values
		

			
			 	csv.writerow(values)
        	

print "# Tweets Imported:", tweet_count
#print "# Tweets Accummulated:", Acc_Tweets

out1.close()
#out_time1.close()
