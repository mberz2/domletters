import sys
import string
from collections import Counter as ctr
import re

alphabet = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ\n')
words = []
final = []

def is_ascii(s):
	return all(c in alphabet for c in s)

with open(sys.argv[1], "r") as f:
	for l in f:
		words.extend(l.split(" "))

for w in words:
	w = w.upper()
	if is_ascii(w):
		final.append(ctr(w).most_common(1)[0])
		#print(ctr(w).most_common(1)[0])

count = 0
for key, w in final:
	count += (w)

print(count)