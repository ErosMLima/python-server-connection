def longest_consec(strarr, k):
	consec = []
	for i in range(k):
		if strarr:
			max_string = max(strarr, key=len)
			consec.append(max_string)
			strarr.remove(max_string)
	return "".join(consec)

