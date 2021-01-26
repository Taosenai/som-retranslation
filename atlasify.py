from re import sub, search

dyn_counter = 0
fixed_counter = 0

def banner(match):
	global dyn_counter
	banner = f"// -------- Pointer #{dyn_counter} ({match.group(1)} -> {match.group(2)}) --------\n"
	dyn_counter += 1
	return banner

def clean(s):
	# s = sub(r'//POINTER #\d* @ (\$.*?) - STRING #\d* @ (\$.*?)\n', banner, s) # Prettify event address comments
	s = sub(r'//POINTER #\d* @ (\$.*?) - STRING #\d* @ (\$.*?)\n', '', s) # Delete comments
	s = sub(r'// current address.*?\n', '', s) # Delete address bounds

	return s

def rewrite_commands(s, old, new):
	s = sub(fr"#JMP\(\${old}(.*?), \${old}(.*?)\)", fr"#JMP(${new}\1, ${new}\2)", s)
	s = sub(fr"#HDR\(\${old}(.*?)\)", fr"#HDR(${new}\1)", s)
	s = sub(fr"#W16\(\${old}(.*?)\)", fr"#W16(${new}\1)", s)

	return s