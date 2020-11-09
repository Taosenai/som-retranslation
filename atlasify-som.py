from atlasify import clean, rewrite_commands
import re

with open("script_som.txt", 'r', encoding="utf8") as f:
	s = f.read()
	s = rewrite_commands(s, "9", "21")
	s = rewrite_commands(s, "A", "24")
	s = clean(s)
		
	with open("script_som-atlasify.txt", "w", encoding="utf8") as out:
		out.write(s)

with open("script_som-menu.txt", 'r', encoding="utf8") as f:
	s = f.read()
	s = clean(s)
	s = s.split('\n')
	idx = 0
	while idx < len(s):
		matches = re.search(r'\/\/Block Range: \$(.*?) - \$(.*?)$', s[idx])
		if matches:
			start = matches.group(1)
			end = matches.group(2)
			fixedlen = int(end, 16) - int(start, 16)
			cmd = "#FIXEDLENGTH(%d, 80)\n#JMP($%s)\n" % (fixedlen, start)
			s[idx-1] = f"// -------- Fixed ${start}-${end} ({s[idx-1][20:-1]})\n"
			del s[idx]
			s.insert(idx, cmd)
			s[idx+1] = re.sub(r"\[END\]", "[END]<END>", s[idx+1])
		s[idx] = s[idx] + '\n'
		idx += 1
	s = ''.join(s)

	with open("script_som-menu-atlasify.txt", "w", encoding="utf8") as out:
		out.write(s)

print("Atlasify done")