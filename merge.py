import re

def merge(source, dest):
	f1 = open(source, 'r', encoding="utf8")
	f2 = open(dest, 'r', encoding="utf8")

	lines_sd2 = f1.readlines()
	lines_turbo = f2.readlines()

	idx_sd2 = 0
	idx_turbo = 0

	pattern_kanjikana = r"([\u3300-\u33ff\ufe30-\ufe4f\uf900-\ufaff\U0002f800-\U0002fa1f\u30a0-\u30ff\u2e80-\u2eff\u4e00-\u9fff\u3400-\u4dbf\U00020000-\U0002a6df\U0002a700-\U0002b73f\U0002b740-\U0002b81f\U0002b820-\U0002ceaf]+)"

	while idx_sd2 < len(lines_sd2):
		line_sd2 = lines_sd2[idx_sd2]
		groups = re.findall(r'\/\/ -------- Pointer #(\d*?) \(', line_sd2)
		has_match = len(groups) > 0
		if not has_match:
			idx_sd2 += 1
			continue

		event_num = groups[0]

		while idx_turbo < len(lines_turbo) - 1:
			line_turbo = lines_turbo[idx_turbo]
			is_event = re.search(r'\/\/ -------- Pointer #%s \(' % event_num, line_turbo) != None
			if not is_event:
				idx_turbo += 1
				continue

			while idx_sd2 < len(lines_sd2) - 1:
				nextline_sd2 = lines_sd2[idx_sd2+1]
				contains_jpn = re.search(pattern_kanjikana, nextline_sd2) != None
				if contains_jpn:
					cleanline = re.sub(r"\[.*\]", '', nextline_sd2)
					cleanline = re.sub(r"\<.*\>", '', cleanline)
					lines_turbo.insert(idx_turbo + 2, "// SD2: %s" % cleanline )
					idx_turbo += 1
					idx_sd2 += 1
					continue
				if nextline_sd2.startswith("//"):
					break
				idx_sd2 += 1
			idx_turbo += 1
			break

		idx_sd2 += 1

	out = open("merged-script_%s+%s.txt" % (source, dest), 'w', encoding="utf8")
	out.writelines(lines_turbo)

			
			


			







