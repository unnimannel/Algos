log_content = open('syslog','r')
entry_time = 'NA'
occurance = 0
for line in log_content:
	try:
		if entry_time == line[:15]:
			occurance = occurance + 1
		else:
			if occurance > 0:
				print(entry_time,' : ',occurance)
			entry_time = line[:15]
			occurance = 1
	except Exception:
		pass