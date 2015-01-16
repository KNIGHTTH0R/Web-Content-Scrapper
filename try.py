#!/usr/bin/env python
search_list_url="http://www.rottentomatoes.com/m/the-croods/reviews/#"
#req=urllib2.Request(search_list_url,headers={'User-agent:','Mozilla/5.0'})
flag=1
links = []
while flag==1:
	
	page=urllib2.urlopen(search_list_url)
	soup=BeautifulSoup(page)

	for link in soup.findAll('a'):
		if str(link).find("Full Review")>0:
			links.append(str(link.get('href')))

	for link in soup.findAll('a'):
		if str(link).find("button pagination right")>0:
			search_list_url="http://www.rottentomatoes.com"+link.get('href')
			flag=1
			print search_list_url
			break
			

        else:
             flag=0	

