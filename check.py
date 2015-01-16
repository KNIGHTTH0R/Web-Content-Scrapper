def scrap_review(url,n,path):
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
        
    myfile=open(path+"/review"+str(n)+".txt",'w')
    for text in review:
        myfile.write(text)

    myfile.close()

review_list_url="http://www.rottentomatoes.com/m/the-croods/reviews/#"
#req=urllib2.Request(review_list_url,headers={'User-agent:','Mozilla/5.0'})
n=1
flag=1
while flag==1:
    
    review_list_page=urllib2.urlopen(review_list_url)
    review_list_soup=BeautifulSoup(review_list_page)

    for div in review_list_soup.findAll('div',{"class":"media_block_content"}):
        for div2 in div.findAll('div'):
            for rating in div2.findAll('div'):
                if str(rating).find("small rotten")>0:
                    for review in div.findAll('a'):
                        if str(review).find("Full Review")>0:
                            review_url=review.get("href")
                            scrap_review(review_url,n,path2)
                            n=n+1

                elif str(rating).find("small fresh")>0:
                    for review in div.findAll('a'):
                        if str(review).find("Full Review")>0:
                            review_url=review.get("href")
                            scrap_review(review_url,n,path1)
                            n=n+1
                            



    for link in review_list_soup.findAll('a'):
        if str(link).find("button pagination right")>0:
            review_list_url="http://www.rottentomatoes.com"+link.get('href')
            flag=1
            break
            

        else:
             flag=0 

