#File Objects

#using context mananger
with open('test.txt','r') as f:
	#for line in f: #iterate over the lines in file
		#print(line,end= '')
	#f_contents = f.readline()
	#f_contents = f.readlines() prints a list of  the lines in the file
	#print(f_contents)
	#f_contents = f.read(100) # read the 100  lines of the file
	#print(f_contents,end = '')

	# When size of file is unknown
	#size_to_read = 10 #printing by 10 characters each 
	#f_contents = f.read(size_to_read)
	#print(f_contents,end = '')
	#f.seek(0)
	#manipulate currnet position using f.seek() method
	#f_contents = f.read(size_to_read)
	#print(f_contents)
	
	#see the current postion using f.tell
	#print(f.tell())
	#while len(f_contents)> 0: 
	#	print(f_contents,end = '*')
	#	f_contents = f.read(size_to_read)
	

	

