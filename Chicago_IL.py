#author: Honey Singh
#10/13/2014

#Import ftplib to transfer file from CDoT
from ftplib import FTP
import sys
import string

def finding():
	ftps = FTP('ftp.travelmidwest.com')
	# opening ftp
	ftps.login('purdueececam2','ca%m2$pur&du9e')
	rptr = open('filedata','w') 
	#writing the data into a local file
	ftps.retrbinary('RETR /cameraInfo.txt', rptr.write)
	ne = open('filedata','r')
	# opening the data file 
	test = ne.readlines()
	# reading each line ending with '\n'
	f = open('Chicago_IL','w')
	ls = [] # creating a list to store each tuple
	count = 0
	for i in range(0,len(test)-1):
		k = 0
		le = len(test[i])
		while k < le :
			# looping to partition data 
			t = test[i].partition("|")
		# adding partitioned data to list
			ls.append(t[0])
			k = k + 1
		# moving on to next part of string to partition
			test[i] = t[2]
		ls[2] = float(ls[2])/100000
		# original data did not have decimal
		ls[3] = float(ls[3])/100000
		# writing each element of tuple saved in list
		f.write(ls[1]+"#Chicago#IL#USA#"+"ftp://ftp.travelmidwest.com/"+ls[0]+"#"+str(ls[2])+"#"+str(ls[3])+"\n")
		
		count = 0

	rptr.close()
	ne.close()
	f.close()
finding()
