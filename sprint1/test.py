
import xmltodict
import json
import urllib.request
import csv


def readNASAExoplanetArchive():
    
    url = "http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&format=json"
    data = urllib.request.urlopen(url).read().decode('utf-8')
    a = json.loads(data)
    print(a)

    
# Needs some fixing reading CSV files
def readExoplaneteu():
    
    url = "http://exoplanet.eu/catalog/csv/"
    data = urllib.request.urlopen(url).read().decode('utf-8')
    cat = {}
    data = data.split("\n")
    for line in data:
    	temp = line.split(",")
    	cat[temp[0]] = temp[1:]
    print(cat)
    
def readOEC():
    
    result = xmltodict.parse("""<system>
	    <name>KOI-0001</name>
	    <rightascension>19 07 14</rightascension>
	    <declination>+49 18 59</declination>
	    <distance>224.03</distance>
	    <star>
	            <magB errorminus="0.10" errorplus="0.10">11.85</magB>
	            <magV errorminus="0.08" errorplus="0.08">11.25</magV>
	            <magJ errorminus="0.020" errorplus="0.020">10.232</magJ>
	            <magH errorminus="0.026" errorplus="0.026">9.920</magH>
	            <magK errorminus="0.022" errorplus="0.022">9.846</magK>
	            <name>KOI-0001</name>
	            <temperature errorminus="50.00" errorplus="50.00">5814.00</temperature>
	            <radius errorminus="0.1100" errorplus="0.1100">1.0600</radius>
	            <mass errorminus="0.0370" errorplus="0.0370">0.9950</mass>
	            <age errorminus="2.5000" errorplus="2.5000">6.5000</age>
	            <planet>
	                    <name>KOI-0001 b</name>
	                    <name>KOI-0001 01</name>
	                    <radius errorminus="0.14581" errorplus="0.14581">1.31228</radius>
	                    <period errorminus="9.0000000e-08" errorplus="9.0000000e-08">2.470613170000</period>
	                    <transittime errorminus="0.0000097" errorplus="0.0000097">2454955.7625662</transittime>
	                    <semimajoraxis>0.0360000</semimajoraxis>
	                    <temperature>1394.0</temperature>
	                    <list>Kepler Objects of Interest</list>
	                    <description>This is a Kepler Object of Interest from the Q1-Q12 dataset. It has been flagged as a possible transit event but has not been confirmed to be a planet yet.</description>
	                    <istransiting>1</istransiting>
	            </planet>
	    </star>
    </system>""")
	
    print(result)    


#readExoplaneteu()
#readExoplanetArchive()
readOEC()