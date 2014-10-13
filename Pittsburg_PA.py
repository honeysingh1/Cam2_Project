from bs4 import BeautifulSoup
import urllib2
import re
import sys
import json

def finding():
	url ="http://www.dot.state.pa.us/Penndot/Districts/district11.nsf/District11TrafficCams"
	soup = BeautifulSoup(urllib2.urlopen(url).read())
	f =open('Pittsburg_PA','w')
	ls = []
	ls2 =[]
	lat =[]
	lon = []
	for link in soup.find_all('a'):
		ls.append('http://www.dot.state.pa.us'+link.get('href')+"#")
		ls2.append(str(link.string))
	for i in range(1,len(ls)-1):
		locat = str(ls2[i]).replace(' ','%20')+",PA,USA"
		jsurl = "https://maps.googleapis.com/maps/api/geocode/json?address="+locat
		url2 = urllib2.urlopen(jsurl).read()
		jsonrs = json.loads(url2)
		lat.append(json.dumps([s['geometry']['location']['lat']for s in jsonrs['results']], indent = 4))
		lon.append(json.dumps([s['geometry']['location']['lng']for s in jsonrs['results']], indent = 4))
		lat[0] = str(lat[0]).replace('[','').replace(']','').replace(' ','').replace('\n','')
		lon[0] = str(lon[0]).replace('[','').replace(']','').replace(' ','').replace('\n','')
		f.write(str(ls[i])+lat[0]+"#"+lon[0]+"#"+str(ls2[i])+"#PA#USA\n")
	f.close()
finding()
