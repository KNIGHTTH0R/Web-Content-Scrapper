links = []
page=urllib2.urlopen(review_url)
soup=BeautifulSoup(page)
i=1
for review in soup.findAll('a'):
	if str(review).find("Full Review")>0:
		links.append(str(review.get('href')))
		print i 
		i=i+1 