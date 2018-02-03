from django.shortcuts import render

import requests
import urllib.parse

def tsearch(request):
	if request.method == "GET":
		qs = request.GET.get('q')
		if qs is not None:
			leetxt = "https://thepiratebay.org/search/"+str(qs)+"/0/99/0"
			url1 = requests.get(leetxt)
			text = url1.text
			##Smaple  Validation 
			url1.name1 = text[text.find('<h2>')+4:text.find('</h2>')][:200867]
			error = url1.name1
			error = error.split(" ")
			if error[4] == "Try":
			    context = {
			    	"error": str(qs)+" Keyword Not Found in this server"
			    }
			else:
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
				#ran = len(link)
				#print(ran)
				# alltag = []
				# for l in range(0,ran):
				#     tag = "<a href='"+link[l]+"'>"+name1[l]+"</a>"
				#     alltag.append(tag)
				context = {
					"li1": link[0],
					"na1": name1[0],
					"li2": link[1],
					"na2": name1[1],
					"li3": link[2],
					"na3": name1[2],
					"li4": link[3],
					"na4": name1[3],
					"li5": link[4],
					"na5": name1[4],
					"li6": link[5],
					"na6": name1[5],
					"li7": link[6],
					"na7": name1[6],
					"li8": link[7],
					"na8": name1[7],
					"li9": link[8],
					"na9": name1[8],
					"li10": link[9],
					"na10": name1[9],
					"li11": link[10],
					"na11": name1[10],
					"li12": link[11],
					"na12": name1[11],
					"li13": link[12],
					"na13": name1[12],
					"li14": link[13],
					"na14": name1[13],
					"li15": link[14],
					"na15": name1[14],
					"li16": link[15],
					"na16": name1[15],
					"li17": link[16],
					"na17": name1[16],
					"li18": link[17],
					"na18": name1[17],
					"li19": link[18],
					"na19": name1[18],
					"li20": link[19],
					"na20": name1[19],
					"li21": link[20],
					"na21": name1[20],
					"li22": link[21],
					"na22": name1[21],
					"li23": link[22],
					"na23": name1[22],
					"li24": link[23],
					"na24": name1[23],
					"li25": link[24],
					"na25": name1[24],
					"li26": link[25],
					"na26": name1[25],
					"li27": link[26],
					"na27": name1[26],
					"li28": link[27],
					"na28": name1[27],
					"li29": link[28],
					"na29": name1[28],
					"success": "Torrent Search Result for "+str(qs)
					}
		else:
			context = {
			"nferror": "Your Request not found in this server"
			}
			return render(request, "home/404.html", context)
	return render(request, "home/search.html", context)


def SearchHome(request):
	if request.method == "GET":
		qs = request.GET.get('q')
		if qs is not None:
			leetxt = "https://thepiratebay.org/search/"+str(qs)+"/0/99/0"
			url1 = requests.get(leetxt)
			text = url1.text
			##Smaple  Validation 
			url1.name1 = text[text.find('<h2>')+4:text.find('</h2>')][:200867]
			error = url1.name1
			error = error.split(" ")
			if error[4] == "Try":
			    context = {
			    	"error": str(qs)+" Keyword Not Found in this server"
			    }
			else:
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
				#ran = len(link)
				#print(ran)
				# alltag = []
				# for l in range(0,ran):
				#     tag = "<a href='"+link[l]+"'>"+name1[l]+"</a>"
				#     alltag.append(tag)
				context = {
					"li1": link[0],
					"na1": name1[0],
					"li2": link[1],
					"na2": name1[1],
					"li3": link[2],
					"na3": name1[2],
					"li4": link[3],
					"na4": name1[3],
					"li5": link[4],
					"na5": name1[4],
					"li6": link[5],
					"na6": name1[5],
					"li7": link[6],
					"na7": name1[6],
					"li8": link[7],
					"na8": name1[7],
					"li9": link[8],
					"na9": name1[8],
					"li10": link[9],
					"na10": name1[9],
					"li11": link[10],
					"na11": name1[10],
					"li12": link[11],
					"na12": name1[11],
					"li13": link[12],
					"na13": name1[12],
					"li14": link[13],
					"na14": name1[13],
					"li15": link[14],
					"na15": name1[14],
					"li16": link[15],
					"na16": name1[15],
					"li17": link[16],
					"na17": name1[16],
					"li18": link[17],
					"na18": name1[17],
					"li19": link[18],
					"na19": name1[18],
					"li20": link[19],
					"na20": name1[19],
					"li21": link[20],
					"na21": name1[20],
					"li22": link[21],
					"na22": name1[21],
					"li23": link[22],
					"na23": name1[22],
					"li24": link[23],
					"na24": name1[23],
					"li25": link[24],
					"na25": name1[24],
					"li26": link[25],
					"na26": name1[25],
					"li27": link[26],
					"na27": name1[26],
					"li28": link[27],
					"na28": name1[27],
					"li29": link[28],
					"na29": name1[28],
					"success": "Torrent Search Result for "+str(qs)
					}
		else:
			context = {
			"nferror": "Your Request not found in this server"
			}
			return render(request, "home/404.html", context) 
	return render(request, "home/home.html", context)