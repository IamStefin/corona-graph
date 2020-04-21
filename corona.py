#!/usr/bin/env python3 
import requests
import json
import matplotlib.pyplot as plt

c = input("Country Name:")
url = "https://pomber.github.io/covid19/timeseries.json"

date = []

conf = []
conf_us = []
html_doc = requests.get(url).text
json_data = json.loads(html_doc)
for i in range(len(json_data[c])):
   print(str(json_data[c][i]['date']) + "----->Confirmed:" + str(int(json_data[c][i]['confirmed'])-int(json_data[c][i-1]['confirmed'])))
   date.append(json_data[c][i]['date'])
   conf.append(json_data[c][i]['confirmed']-json_data[c][i-1]['confirmed'])
conf[0]=json_data[c][0]['confirmed']
plt.plot(date,conf,label=c)
plt.xlabel('Date') 
# naming the y axis 
plt.ylabel('Confirmed Cases') 

# giving a title to my graph 
plt.title("Analysis") 
plt.legend() 
# function to show the plot 
plt.show() 