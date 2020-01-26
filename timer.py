import time

# How can we change it so that it will open the file, find the current time already logged, and add it to the final result instead of adding a whole bunch of times over and over again?
# Or create a new program to sum the total amount of log time.

def start():
	start = time.time()
	print("Now logging time")
	s = input()
	if s == "stop":
		end = time.time()
		f = open('logtimes', 'a')
		f.write(str(end - start) + '\n')
		f.close()
		print("Done logging time")
		quit()
	#todo add a status that prints the current time elapsed
start()
