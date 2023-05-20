import sys
from tqdm import tqdm
from nlgeval import NLGEval

f1 = open(sys.argv[1], 'r')
f2 = open(sys.argv[2], 'r')

references = list()
hypotheses = list()

l1 = f1.readlines()
l2 = f2.readlines()

num = len(l2)

for i in range(num):
	hypotheses.append(l2[i][:-1])
	rr = [ l1[i*5][:-1], l1[i*5+1][:-1], l1[i*5+2][:-1], l1[i*5+3][:-1], l1[i*5+4][:-1] ]
	references.append(rr)

nlgeval = NLGEval()

metrics_dict = nlgeval.compute_metrics(references, hypotheses)
print(metrics_dict)
