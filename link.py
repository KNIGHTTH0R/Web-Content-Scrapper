url="http://www.rottentomatoes.com/m/pirates_of_the_caribbean_the_curse_of_the_black_pearl/"
page=urllib2.urlopen(url)
movie_soup=BeautifulSoup(page)
links = []
for link in movie_soup.findAll('a'):
	if str(link).find(" all critic reviews")>0:
		print link.get('href')
		review_list_url="http://www.rottentomatoes.com"+link.get('href')
