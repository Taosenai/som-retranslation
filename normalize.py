import unicodedata

with open("sd2ji.tbl", "r", encoding="utf8") as f:
	s = f.read()
	n = unicodedata.normalize('NFC', s)
	
	with open("sd2ji-nfc.tbl", "w", encoding="utf8") as f2:
		f2.write(n)


