import csv
from collections import defaultdict


    

with open('2015_Cyclone_Pam_en.csv', 'rb') as f:
    r = csv.reader(f)
    r.next()
    dict1 = {row[1]: row[0] for row in r}
    #print dict1
   
    

#with open('b.csv', 'rb') as f:
    #r = csv.reader(f)
    #dict2 = {row[0]: row[1:] for row in r}
columns = defaultdict(list)
with open('FromJsontoRaw2015_Cyclone_Pam_en.csv', 'rU') as f: 
	#with codecs.open(csvfile, "r", "utf-8") as f:
		reader = csv.DictReader(f) # read rows into a dictionary format
		for row in reader: # read a row as {column1: value1, column2: value2,...}
			for (k,v) in row.items(): # go over each column name and value 
				columns[k.strip()].append(v) # append the value into the appropriate list based on column name k
				if (k=='id'):
					#print v
					columns['label'].append(dict1["'"+v+"'"])   
					#print columns['label']
					

with open("ab_combined_2015_nepal_eq_cf_labels.csv", 'wb') as f:
	
		writer = csv.writer(f,quoting=csv.QUOTE_ALL)
		writer.writerow(['id','created_at','text','label'])
		rows = zip(columns['id'],columns['created_at'],columns['text'],columns['label'])
		for row in rows:
			writer.writerow(row)

