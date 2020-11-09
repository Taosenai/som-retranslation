from atlasify import clean
import re

with open("script_turbo-vwf.txt", 'r', encoding="utf8") as f:
	s = f.read()
	s = clean(s)
		
	with open("script_turbo-vwf-atlasify.txt", "w", encoding="utf8") as out:
		out.write(s)