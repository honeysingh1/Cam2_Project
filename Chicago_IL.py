
from ftplib import FTP
import sys
import string
#from StringIO import StringIO

def finding():
	ftps = FTP('ftp.travelmidwest.com')
	ftps.login('purdueececam2','ca%m2$pur&du9e')
#ftps.retrlines('LIST')
	r = open('filedata','w') 
	ftps.retrbinary('RETR /cameraInfo.txt', r.write)
	ne = open('filedata','r')
	test = ne.readlines()
	f = open('Chicago_IL','w')

	for i in range(0,len(test)-1):
		test[i] = test[i].replace('|','#').replace('\n','#IL#USA\n')
		f.write("ftp://ftp.travelmidwest.com/"+test[i])

	r.close()
	ne.close()
	f.close()
finding()
