

import sys
import json
fname = sys.argv[1]

queries = list()
count = 1
fname_pure = fname.split('/')[-1]
contains_names = False
with open(fname, 'r') as f:
	line = f.readline().strip()
	while line:
		# check if query file containes query names
		
		parts = line.split('\t')
		if len(parts) > 1:
			# use query name
			query_name =  parts[0]
			query = parts[1]
			contains_names = True
		else:
			query_name = fname_pure[:3] + str(count)
			query = parts[-1]
		queries.append({ 'number': query_name , 'text': '#dirichlet(' + query + ')' })
		count += 1
		line = f.readline().strip()

js = {'casefold': False, 'queries': queries}

if not contains_names:
	with open(fname + '.names', 'w') as f:
		for q in queries:
			f.write(q['number'] + '\t' + q['text'] + '\n')

with open(fname + '.json', 'w') as f:
    json.dump(js, f)
