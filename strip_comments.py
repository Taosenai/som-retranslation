import sys
from os import path

fn = sys.argv[1]

with open(fn, "r", encoding="utf-8") as f:
	with open("stripped_" + path.basename(fn), "w", encoding="utf-8") as o:
		for line in f.readlines():
			if line.startswith("// SD2"):
				o.write(line)
				continue
			if not line.startswith("//") and not line == "\n":
				o.write(line)

