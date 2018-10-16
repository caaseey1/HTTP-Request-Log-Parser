# https://s3.amazonaws.com/tcmg476/http_access_log

#Questions (Output to screen)
# How many total requests were made in the time period represented in the log?
# How many requests were made on each day? per week? per month?
# What percentage of the requests were not successful (any 4xx status code)?
# What percentage of the requests were redirected elsewhere (any 3xx codes)?
# What was the most-requested file?
# What was the least-requested file?

# Logs should be broken into separate files by month 
# Write the 12 files to this directory (~/Desktop/Project3)

import urllib.request #downloading a file over the internet
import re #regular expressions
from pathlib import Path
import operator


log_url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local_log_file = Path("logfile.txt")

# Retrieve File
if local_log_file.is_file():
	#file exists
	print("Log file exists!\n")
else: #file does not exist
	print("Downloading log file now!\n")
	urllib.request.urlretrieve(log_url, 'logfile.txt')

# Separating Log file by month
outfile1 = open('January.txt', 'w')
outfile2 = open('February.txt', 'w')
outfile3 = open('March.txt', 'w')
outfile4 = open('April.txt', 'w')
outfile5 = open('May.txt', 'w')
outfile6 = open('June.txt', 'w')
outfile7 = open('July.txt', 'w')
outfile8 = open('August.txt', 'w')
outfile9 = open('September.txt', 'w')
outfile10 = open('October.txt', 'w')
outfile11 = open('November.txt', 'w')
outfile12 = open('December.txt', 'w')


#variables
count = 0 # number of lines or number of requests
#months
jancount = 0
febcount = 0
marcount = 0
aprcount = 0
maycount = 0
juncount = 0
julcount = 0
augcount = 0
sepcount = 0
octcount = 0
novcount = 0
deccount = 0

week = 0
day = 0
xx4 = 0
xx3 = 0

leastcount = 0

num_files = {}

#i = 0

# For loop to answer questions
for line in open(local_log_file): 
	count += 1 #amount of requests
	#lines = local_log_file.readline()
	#Month dividing

	#t.write("bin: "+line.strip()+"\n")

	if bool(re.match('.*Jan.*',line.strip())):
		outfile1.write(line.strip()+"\n")
		jancount += 1
	elif bool(re.match('.*Feb.*',line.strip())):
		outfile2.write(line.strip()+"\n")
		febcount += 1
	elif bool(re.match('.*Mar.*',line.strip())):
		outfile3.write(line.strip()+"\n")
		marcount += 1
	elif bool(re.match('.*Apr.*',line.strip())):
		outfile4.write(line.strip()+"\n")
		aprcount += 1
	elif bool(re.match('.*May.*',line.strip())):
		outfile5.write(line.strip()+"\n")
		maycount += 1
	elif bool(re.match('.*Jun.*',line.strip())):
		outfile6.write(line.strip()+"\n")
		juncount += 1
	elif bool(re.match('.*Jul.*',line.strip())):
		outfile7.write(line.strip()+"\n")
		julcount += 1
	elif bool(re.match('.*Aug.*',line)):
		outfile8.write(line.strip()+"\n")
		augcount += 1
	elif bool(re.match('.*Sep.*',line.strip())):
		outfile9.write(line.strip()+"\n")
		sepcount += 1
	elif bool(re.match('.*Oct.*',line.strip())):
		outfile10.write(line.strip()+"\n")
		octcount += 1
	elif bool(re.match('.*Nov.*',line.strip())):
		outfile11.write(line.strip()+"\n")
		novcount += 1
	elif bool(re.match('.*Dec.*',line.strip())):
		outfile12.write(line.strip()+"\n")
		deccount += 1
	else:
		...

	#request type
	if bool(re.match('.*[3][0-9][0-9]',line)):
		xx3 += 1
	elif bool(re.match('.*[4][0-9][0-9]',line)):
		xx4 += 1
	else:
		...

	# most/least requested file (DICT)
	words = line.split(" ")
	#print("words ", words)
	for i in range(len(words)):
		if words[i] == '"GET' and i+1 < len(words):
			filename = words[i+1]

			if filename in num_files:
				num_files[filename] += 1
			else:
				num_files[filename] = 1
	#dictionary needs to be sorted == num_files
	
#sort dictionary outside of loop
sort_files = sorted(num_files.items(),key = operator.itemgetter(1),reverse = True)

# Print Statements
print("length of numfiles", len(num_files))

week = count/52
day = count/365
print("Total requests: ",count,"\n")

print("In the local directory of this python file are new log files separated by month.")
print("Requests in January: ",jancount)
print("Requests in February: ",febcount)
print("Requests in March: ",marcount)
print("Requests in April: ",aprcount)
print("Requests in May: ",maycount)
print("Requests in June: ",juncount)
print("Requests in July: ",julcount)
print("Requests in August: ",augcount)
print("Requests in September: ",sepcount)
print("Requests in October: ",octcount)
print("Requests in November: ",novcount)
print("Requests in December: ",deccount,"\n")

print("Average requests per week: "+"{:.2f}".format(week))
print("Average requests per day: "+"{:.2f}".format(day)+"\n")

print("This is the most requested file ('filename', amount of requests): \n ", sort_files[0],"\n")
print("Out of the 12,178 files requested, multiple files were requested only once.")
print("This is an example of a file requested only once:",sort_files[12176],"\n")

print("Total unsuccessful attempts: ",xx4)
print("Total requests that were redirected: ",xx3,"\n")
