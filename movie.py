#url="http://www.rottentomatoes.com/search/?search=s&sitesearch=rt#results_movies_tab"
#page=urllib2.urlopen(url)
#soup=BeautifulSoup(page)
i=1

for movie in soup.findAll('div',{"class":"media_block_content"}):
	if len(movie.findAll('ul'))==0:
		for m in movie.findAll('a'):
			if str(m).find("_top")>=0:
				print m.get('href')
				print i
				i=i+1
	
