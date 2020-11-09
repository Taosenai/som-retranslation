from atlasify import clean
import jpn2hex
import re

with open("script_sd2.txt", 'r', encoding="utf8") as f:
	s = f.read()
	s = clean(s)
		
	with open("script_sd2-atlasify.txt", "w", encoding="utf8") as out:
		out.write(s)

	with open("script_sd2-atlasify-hex.txt", "w", encoding="utf8") as out:
		s = jpn2hex.convertlines(s)
		out.write(s)

print("Atlasify done")