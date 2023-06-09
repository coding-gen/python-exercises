#! /usr/bin/python3


import sys

t = sys.argv[1]
out_text = ""
exceptions = ["THE", "AND", "WITH", "OF", "FOR", "BY", "VIA", "IN", "TO", "A"]
for word in t.split():
	if word in exceptions:
		out_text += " " + word.lower()
	else: 
		out_text += " " + word[:1] + word[1:].lower()
print(out_text.strip())