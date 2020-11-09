# Put a complete script with script tags in corpus.txt and run this
# to generate the most efficient DTE table for the text.

from collections import Counter

bin2alpha = {
	"80": " ",
	"81": "a",
	"82": "b",
	"83": "c",
	"84": "d",
	"85": "e",
	"86": "f",
	"87": "g",
	"88": "h",
	"89": "i",
	"8A": "j",
	"8B": "k",
	"8C": "l",
	"8D": "m",
	"8E": "n",
	"8F": "o",
	"90": "p",
	"91": "q",
	"92": "r",
	"93": "s",
	"94": "t",
	"95": "u",
	"96": "v",
	"97": "w",
	"98": "x",
	"99": "y",
	"9A": "z",
	"9B": "A",
	"9C": "B",
	"9D": "C",
	"9E": "D",
	"9F": "E",
	"A0": "F",
	"A1": "G",
	"A2": "H",
	"A3": "I",
	"A4": "J",
	"A5": "K",
	"A6": "L",
	"A7": "M",
	"A8": "N",
	"A9": "O",
	"AA": "P",
	"AB": "Q",
	"AC": "R",
	"AD": "S",
	"AE": "T",
	"AF": "U",
	"B0": "V",
	"B1": "W",
	"B2": "X",
	"B3": "Y",
	"B4": "Z",
	"BF": ".",
	"C0": ",",
	"C1": "/",
	"C2": "'",
	"C3": "“",
	"C4": "”",
	"C5": ":",
	"C6": "-",
	"C7": "%",
	"C8": "!",
	"C9": "&",
	"CA": "?",
	"CB": "(",
	"CC": ")",
	"CD": "#",
	"CE": "▼",
	"CF": "←",
	"D0": "→",
	"D1": "↑",
	"D2": "↓"
}
alpha2bin = {v: k for k, v in bin2alpha.items()}

def find_replace(string, dictionary):
    for item in string:
        if item in dictionary.keys():
            string = string.replace(item, dictionary[item])
    return string

with open("corpus.txt", "r", encoding="utf8") as f:
	s = f.read()

	dte_pairs = []
	pairs = []

	# Terrible slow algo but I don't care
	for i in range(0,61): # 61 possible DTE
		j = 0
		while j < len(s):
			pair = s[j:j+2]
			if (pair not in dte_pairs) and (pair != '  ') and ('*' not in pair):
				pairs.append(pair)
			j += 2

		most_common = Counter(pairs).most_common(5)
		# print("%d: %s" % (i, most_common))
		dte_pairs.append(most_common[0][0])
		pairs = []

	print("-------------------")
	print(dte_pairs)
	print("%s pairs" % len(dte_pairs))

	print("-------------------")

	print('\n\nNew DTE Table\n\n')

	j = 0
	for i in range(96, 125): # $60-$7C
		print("%s=%s" % (hex(i)[2:].upper(), dte_pairs[j]))
		j += 1
	print('\n\n')
	
	j -= 14 # 13 DTE characters overlap in the table 
	for i in range(211, 256): # $D3-$FF
		print("%s=%s" % (hex(i)[2:].upper(), dte_pairs[j]))
		j += 1

	print("\n\nHex blob to insert at $077299-$077312")
	dte_blob = ''.join(dte_pairs)
	print(find_replace(dte_blob, alpha2bin))
	print("(%d bytes)" % len(dte_blob))
		

