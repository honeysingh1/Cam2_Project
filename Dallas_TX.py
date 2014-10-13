#!/usr/bin/python

import urllib2
import re
import sys
import string

def finding():

	Dallas_url= "http://dfwtraffic.dot.state.tx.us/DalTrans/GetFile.aspx?FileName=MapBurnerOutput/Cameras.js"
	soup = urllib2.urlopen(Dallas_url).read()
	f = open('Dallas_TX','w')
	ls1 = []   #created 4 lists
	ls2 = []   #to store id of image snapshot 
	ls3 = []   #and the description and Geos
	ls4 = []  
	test = re.findall(r'cc[(]["].*[)][;]',soup)
# reg exp to find the list of cameras
	for i in range(0,len(test)-1):
		test[i] = test[i].replace('cc(','')
		test[i] = test[i].replace(', ','$')
		test[i] = test[i].replace('"','')
		test[i] = test[i].replace('#','')
# replacing special chars
		i = 0
		count = 0  #counter to only get 4 values

		'''The code starts looking from first line of details of camera in the source file. Then, a 2-D array looks at each character. If the char is not '$', which I manually added for better boundary, the char is added in simultaneous list. Then, it is checked if we reached the first boundary '$'. If true, the list is edited to replace all special charactersand then printed in the desired format'''

	while i < len(test):
		for j in range(0, len(test[i])/2):
			if test[i][j]!='$'and count == 0 :
				ls1.append(test[i][j])
			elif test[i][j] !='$'and count == 1:
				ls2.append(test[i][j])
			elif test[i][j] != '$'and count ==2:
				ls3.append(test[i][j])
			elif test[i][j] != '$'and count ==3:
				ls4.append(test[i][j])
			elif test[i][j] =='$'and count == 0:
				ls1=str(ls1).replace('\'','').replace(']','').replace(' ','')
				ls1=str(ls1).replace('[','').replace(',','') 
				f.write("http://dfwtraffic.dot.state.tx.us/DalTrans/CameraSnapshots/"+str(ls1)+".jpg#")
				count = count + 1
				ls1 = []
			elif test[i][j] =='$'and count == 2:
				ls3=str(ls3).replace('\'','').replace(']','').replace(' ','')
				ls3=str(ls3).replace('[','').replace(',','')
				f.write(str(ls3)+"#")
				count = count + 1
				ls3 = []
			elif test[i][j] =='$'and count == 3:
				ls4=str(ls4).replace('\'','').replace(']','').replace(' ','')
				ls4=str(ls4).replace('[','').replace(',','') 
				f.write(str(ls4)+"#TX#USA\n")
				count = count + 1
				ls4 = []
			elif test[i][j] =='$'and count == 1:
				ls2=str(ls2).replace('\'','').replace(']','')
				ls2=str(ls2).replace('[','').replace(',','').replace('  ','~').replace(' ','') 
				ls2 = str(ls2).replace('~',' ')
				f.write(str(ls2)+"#")
				count = count + 1
				ls2 = []
				count = 0
	i = i + 1
	f.close()
finding()

