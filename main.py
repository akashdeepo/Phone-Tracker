#pip installs-- phonenumbers,opencage, folium
import phonenumbers
import opencage
import folium
from myphone import number

from phonenumbers import geocoder

#Extracting the location
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,'en')
print(location)

#Service provider name
from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, 'en'))

#for location   
from opencage.geocoder import OpenCageGeocode

key = '3f6215c85a3e41baa010cd469ce9c7d1'
geocoder = OpenCageGeocode(key)
query= str(location)
results = geocoder.geocode(query)
#print(results)
lat= results[0]['geometry']['lat']
lng= results[0]['geometry']['lng']

print(lat,lng)

#use location to plot on maps
myMap = folium.Map(location=[lat,lng], zoom_start= 9)
folium.Marker([lat,lng], popup= location).add_to(myMap)

myMap.save('mylocation.html')