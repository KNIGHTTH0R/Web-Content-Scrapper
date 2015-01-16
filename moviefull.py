url="http://www.rottentomatoes.com/search/ajax/?searchtype=movie&search=d&page=1"
movie_list = []
i=2
while 1<100:
	page=urllib2.urlopen(url)
	soup=BeautifulSoup(page)
	for movie in soup.findAll('div',{"class":"media_block_content"}):
		if len(movie.findAll('ul'))==0:
			for m in movie.findAll('a'):
				if str(m).find("_top")>=0:
					print m.get('href')
					movie_list.append("http://www.reottentomatoes.com"+m.get('href'))

	url="http://www.rottentomatoes.com/search/ajax/?searchtype=movie&search=d&page="+str(i)
	i=i+1