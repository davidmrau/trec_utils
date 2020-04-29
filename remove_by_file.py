# remove query ids (one each line) in a file from trec_results
# usage:
# python3 remove_by_file.py trec_results_file query_ids_file 


import sys
import json
import re


docs = sys.argv[1]
q_ids_file = sys.argv[2]


out = docs + '.filtered'

count_succ = 0
count_err = 0


def filter(id_, ids):
	return id_ in ids

q_ids = open(q_ids_file).readlines()

q_ids = [id_.strip() for id_ in q_ids]
q_ids = set(q_ids)
with open(out, 'w') as out_file:
	with open(docs) as doc_file:
		for line in doc_file:
			spl = line.split(' ')
			q_id = spl[0]
			if not filter(q_id, q_ids):
				out_file.write(line)
			count_succ += 1
			if count_succ % 1000000 == 1000000:
				print(f'Processed {count_succ}m lines.')
