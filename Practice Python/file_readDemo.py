#with open('test.txt','r') as rf:
	#with open('test_copy.txt','w') as wf:
		#for line in rf:
		#	wf.write(line)
	#f.write('Test')
	#f.seek(0)
	#f.write('R')
	#making a copy of text.txt file
# to use binary mode.
with open('viberg.jpg','rb') as rf:
	with open('viberg_copy.jpg','wb') as wf:
		chunk_size = 4096
		rf_chunk = rf.read(chunk_size)
		while len(rf_chunk) > 0:
			wf.write(rf_chunk)
			rf_chunk = rf.read(chunk_size)
	#	for line in rf:
	#		wf.write(line)
