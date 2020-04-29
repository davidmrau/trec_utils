# gets trectext documents as input and outputs docno\ttext
# example usage:

#python3 extract_trectext.py filename



import sys
import json
import re


fname = sys.argv[1]

queries = list()
count_succ = 0
count_err = 0
fname_pure = fname.split('/')[-1]
out_file = fname + '.num_query'

doc = ''
def filter(text):
	text = text.lower()
	return re.sub('[^0-9a-zA-Z ]+', ' ', text)	

def extract(doc):
	text = re.findall(r'<TEXT>(.*?)<\/TEXT>', doc, re.DOTALL)
	num = re.findall(r'<DOCNO>(.*?)<\/DOCNO>', doc, re.DOTALL)
	if len(text) > 0 and len(num) > 0:
		return num[-1], filter(text[-1])
	else:
		return num[-1], ''

def make_elem(num, text):
	return num + '\t' + text + '\n'

with open(out_file, 'w') as out:
	with open(fname, 'r') as f:
		for line in f:
			if '</DOC>' in line:
				doc += line
				doc_name, doc_text = extract(doc)
				if doc_text: 
					count_succ += 1
				else:
					count_err += 1
				out.write(make_elem(doc_name, doc_text))
				doc = ''
			else:
				doc += line

print('Extracted '+ str(count_succ) + ' Docs, with ' + str(count_err) + ' Empty Docs.')
