#author: Honey Singh
#date: 10/15/2014

from bs4 import BeautifulSoup
import urllib2
import re
import sys
import json

def finding():
        url ="http://www.trimarc.org/perl/map_form.pl?map_layers=Camera+Snapshots"
        soup = BeautifulSoup(urllib2.urlopen(url).read())
        f =open('Louisville_KY','w')
	# new lists for storing location and geo location
	ls = []
	lat = []
	lon = []
	#searching for <a> in the soup
	for link in soup.find_all('a'):
                # the url to snapshots is under href
                ls.append('http://www.trimarc.org'+link.get('href')+"#")
        for i in range(0,len(ls)-1):
		#using reg exp to find location description
		locat = re.findall('Location.*Highway',ls[i])
	# editing location string to use for google api
		locat = str(locat).replace('Location','').replace('&',',').replace('Highway','')
		locat = str(locat).replace('\'','').replace('[','').replace(']','')
	
               	jsurl = "https://maps.googleapis.com/maps/api/geocode/json?address"+locat
                # using google map api to get geo location
                url2 = urllib2.urlopen(jsurl).read()
                # reading json file
                jsonrs = json.loads(url2)
                # reading latitude and long from json file
                lat.append(json.dumps([s['geometry']['location']['lat']for s in jsonrs['results']], indent = 4))
		lon.append(json.dumps([s['geometry']['location']['lng']for s in jsonrs['results']], indent = 4))	
		
		# editing location des to print to output
		locat = str(locat).replace(',','#').replace('=','').replace('State','Louisville#').replace('%20',' ')
		# removing special symbols from object
		lat[0] = str(lat[0]).replace('[','').replace(']','').replace(' ','').replace('\n','')

                lon[0] = str(lon[0]).replace('[','').replace(']','').replace(' ','').replace('\n','')
		
		# writing the data in correct format
		f.write(str(locat)+"USA#"+str(ls[i])+ str(lat[0])+"#"+str(lon[0])+"\n")
	
	f.close()
finding()

