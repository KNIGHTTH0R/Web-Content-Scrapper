alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for ch in alphabets:
    i=1
    search_url="http://www.rottentomatoes.com/search/ajax/?searchtype=movie&search="+ch+"&page="+str(i)
    no_movies=0 
    while no_movies==0:
        search_page=urllib2.urlopen(search_url)
        search_soup=BeautifulSoup(search_page)
        for movie in search_soup.findAll('div',{"class":"media_block_content"}):
            if len(movie.findAll('ul'))==0:
                for m in movie.findAll('a'):
                    if str(m).find("_top")>=0:
                        movie_url="http://www.rottentomatoes.com/"+m.get('href')
                        movie_page=urllib2.urlopen(movie_url)
                        movie_soup=BeautifulSoup(movie_page)
                        for title in movie_soup.findAll('title'):
                            s=str(title).replace("<title>","")
                            s=s.replace("</title>","")
                            s=s.replace("Rotten Tomatoes","")
                            p=re.compile('\W')
                            st=re.sub(p,'',s)
                            pth="project/corpus/"+st
                            if not os.path.exists(pth):
                                os.mkdir("project/corpus/"+st)
                                print title
        if len(search_soup.findAll('div',{"class":"media_block_content"}))==0:
            no_movies=1  
        i=i+1          
        search_url="http://www.rottentomatoes.com/search/ajax/?searchtype=movie&search="+ch+"&page="+str(i)
       