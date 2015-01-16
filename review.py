def scrap_review(url,n)	
	page=urllib2.urlopen(url).read()
	page=page.replace("<i>","")
	page=page.replace("</i>","")
	soup=BeautifulSoup(page)
	texts=soup.findAll(text=True)

	def visible(element):
		if element.parent.name in ['style','script','document','head','title']:
			return False
		elif re.match('<!--.*-->',str(element)):
			return False
		return True

	visible_texts=filter(visible,texts)
	for text in visible_texts:
		if str(text).find("<!")>=0 & str(text).find(">")>=0:
			visible_texts.remove(text)
		

	review= []

	for text in visible_texts:
		if len(str(text))>90:
			review.append(str(text))
		
	myfile=open("project/corpus/negative/croods/review"+str(n)+".txt",'w')
	for text in review:
		myfile.write(text)

	myfile.close()
