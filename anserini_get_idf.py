from pyserini.index import pyutils
from pyserini.analysis import pyanalysis
import itertools
import sys
import pickle
import math
# gets vocab file with 1 word per line and the number of total documets in the collection.extracts idf value and writes to dict
# idf as descibed here https://en.wikipedia.org/wiki/Tf%E2%80%93idf 

# usage:
# python3 anserini_get_idf.py vocab_file num_docs

#robust num_docs = 528030 with ./IndexUtils -index ../../../../../collections/robust04_index_anserini_no_stem/ -stats

index_utils = pyutils.IndexReaderUtils('/data/david/collections/robust04_index_anserini/')

fname = sys.argv[1]
num_docs = float(sys.argv[2])

count = 0
error = 0

idf = {}
with open(fname) as f:
	for line in f:
		term = line.strip()
		try:
			# Analyze the term.
			df, cf = index_utils.get_term_counts(term)
			idf[term] = math.log(num_docs/df)
			#print(f'term "{term}": df={df}, cf={cf}')
		except:
			error += 1
		count += 1
print(f'{error}/{count} terms were not found in the corpus.')

pickle.dump(idf, open(fname + '_idf.p', 'wb'))

#for term in itertools.islice(index_utils.terms(), 10):
#    print(f'{term.term} (df={term.df}, cf={term.cf})')
