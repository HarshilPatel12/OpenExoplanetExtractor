import xmltodict
import json
import urllib.request
import csv
import dicttoxml
import collections


def readNASAExoplanetArchive():
    
    url = "http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&format=json"
    data = urllib.request.urlopen(url).read().decode('utf-8')
    a = json.loads(data)
    
    final_catalog = {}
    catalog = {}
    for index in range(0, len(a) - 1):
        
        planet_name = a[index]['pl_hostname']
    
        star = {'temperature': {'@errorplus': a[index]['st_tefferr1'], '@errorminus': a[index]['st_tefferr2'] }, 'name': planet_name, 'radius': {'@errorplus': a[index]['st_raderr1'], '@errorminus': a[index]['st_raderr2']}}
        planet = {'Period': {'@errorplus': a[index]['pl_orbpererr1'], '@errorminus': a[index]['pl_orbpererr2'] }, 'lastupdate': a[index]['rowupdate'], 'name': planet_name, 'semimajoraxis': {'@errorplus': a[index]['pl_orbsmaxerr1'], '@errorminus': a[index]['pl_orbsmaxerr2']}, 'radius': {'@errorplus': a[index]['pl_radjerr1'], '@errorminus': a[index]['pl_radjerr2']}, 'eccentricity': {'@errorplus': a[index]['pl_orbeccenerr1'], '@errorminus': a[index]['pl_orbeccenerr2'] } , 'discoverymethod': a[index]['pl_discmethod'], 'mass': {'@errorplus': a[index]['pl_bmassjerr1'], '@errorminus': a[index]['pl_bmassjerr2']}  }
    
    
        catalog.update( {planet_name: {'name': planet_name, 'rightascension': a[0]['ra_str'], 'distance': {'@errorplus': a[0]['st_disterr1'], '@errorminus': a[0]['st_disterr2']}, 'star': star, 'planet' : planet} } )
    
    final_catalog.update({"System" : catalog})
    print(final_catalog)
