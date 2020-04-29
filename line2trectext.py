# gets one query per line as input, writes in trectext format
# example usage:

#python3 query2trectext.py filename



import sys
import json
fname = sys.argv[1]

queries = list()
count = 1
fname_pure = fname.split('/')[-1]
out_file = fname + '.trectext'
queries = list()

def make_elem(num, text):
	return '<top>\n\n<num> Number: ' +  str(num) + '\n\n<title> ' + text + '\n\n <desc> \n\n </top>\n\n\n\n' 

with open(fname, 'r') as f:
	with open(out_file, 'w') as out:
		line = f.readline().strip()
		while line:
			# check if query file containes query names
			
			query_name = fname_pure[:3] + str(count)
			out.write(make_elem(query_name, line))
			queries.append({ 'number': query_name , 'text': line })
			count += 1
			line = f.readline().strip()

with open(fname + '.names', 'w') as f:
	for q in queries:
		f.write(q['number'] + '\t' + q['text'] + '\n')
