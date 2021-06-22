import sys
import string
from collections import Counter as ctr
import re

print("domletters.py")

alphabet = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ\n')
words = []

def is_ascii(s):
	return all(c in alphabet for c in s)

with open(sys.argv[1], "r") as f:
	for l in f:
		words.extend(l.split(" "))

for w in words:

	count = 0
	w = w.upper()
	if is_ascii(w):
		print(ctr(w).most_common(1)[0])