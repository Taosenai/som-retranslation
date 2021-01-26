import re

def merge(source, dest):
	f1 = open(source, 'r', encoding="utf8")
	f2 = open(dest, 'r', encoding="utf8")

	lines_ref = f1.readlines()
	lines_into = f2.readlines()

	idx_ref = 0
	idx_into = 0

	#pattern_kanjikana = r"([\u3300-\u33ff\ufe30-\ufe4f\uf900-\ufaff\U0002f800-\U0002fa1f\u30a0-\u30ff\u2e80-\u2eff\u4e00-\u9fff\u3400-\u4dbf\U00020000-\U0002a6df\U0002a700-\U0002b73f\U0002b740-\U0002b81f\U0002b820-\U0002ceaf]+)"
	pattern_kanjikana = r"[^\x00-\x7F]"

	while idx_ref < len(lines_ref):
		line_ref = lines_ref[idx_ref]
		groups = re.findall(r'\/\/ -------- Pointer #(\d*?) \(', line_ref)
		has_match = len(groups) > 0
		if not has_match:
			idx_ref += 1
			continue

		event_num = groups[0]

		while idx_into < len(lines_into) - 1:
			line_into = lines_into[idx_into]
			is_event = re.search(r'\/\/ -------- Pointer #%s \(' % event_num, line_into) != None
			if not is_event:
				idx_into += 1
				continue

			while idx_ref < len(lines_ref) - 1:
				nextline_ref = lines_ref[idx_ref+1]
				contains_jpn = re.search(pattern_kanjikana, nextline_ref) != None
				if contains_jpn:
					cleanline = re.sub(r"\[(BOY|GIRL|SPRITE)\]", r"{\1}", nextline_ref)
					cleanline = re.sub(r"\[.*?\]", '', cleanline)
					cleanline = re.sub(r"\<.*?\>", '', cleanline)
					lines_into.insert(idx_into + 2, "// SD2: %s" % cleanline )
					idx_into += 1
					idx_ref += 1
					continue
				if nextline_ref.startswith("//"):
					break
				idx_ref += 1
			idx_into += 1
			break

		idx_ref += 1

	out = open("merged-script_%s+%s.txt" % (source, dest), 'w', encoding="utf8")
	out.writelines(lines_into)

			
			


			







