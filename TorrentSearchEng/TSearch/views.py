from django.shortcuts import render

import requests
import urllib.parse

def SearchHome(request):
	text = []
	text = "movie"
	leetxt = "https://thepiratebay.org/search/"+str(text)+"/0/99/0"
	url1 = requests.get(leetxt)
	text = url1.text
	url1.name1 = text[text.find('<table id="searchResult">')+25:text.find('</table>')][:200050]
	moviename = url1.name1
	moviename = moviename.split('<td class="vertTh">')
	link = []
	name1 = []
	for name in range(1,30):
	    moviename1 = moviename[name].split('<a href="')
	    moviename2 = moviename1[3].split('"')
	    torrentname = moviename2[5]
	    torrentname1 = torrentname.split("</a>")
	    leng = len(torrentname1[0])
	    tname = torrentname1[0][1:leng]
	    moviename2 = moviename1[4].split('"')
	    url = moviename2[0]
	    url = urllib.parse.unquote(url)
	    url = urllib.parse.unquote(url)
	    link.append(url)
	    name1.append(tname)
	    #print(name1, link)
	ran = len(link)
	alltag = []
	for l in range(0,ran):
	    tag = "<a href='"+link[l]+"'>"+name1[l]+"</a></br>"
	    alltag.append(tag)

	context = {
		"alltag": alltag,
		"admin" : "Md Jewele Islam"
		}
	return render(request, "home/home.html", context)