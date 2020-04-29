import subprocess

class TrecEval():
	def __init__(self, trec_eval_path):
		self.path = trec_eval_path
	
	def extract_p20(self, ranking_str):
		
		spl = ranking_str.split('\n')

		return spl	
		
	def score(self, qrel_path, ranking_path):
		output = subprocess.run([self.path, qrel_path, ranking_path],  capture_output=True, text=True)
		p20 = self.extract_p20(output)
		print(p20)

trec_eval = TrecEval('../lib/trec_eval/trec_eval')
trec_eval.score(qrel_path='../collections/robust04_test/qrels.robust2004.txt', ranking_path='../results/robust04_anserini_TREC_test_top_1000_bm25').stdout
