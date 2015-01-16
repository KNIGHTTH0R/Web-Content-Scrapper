alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print "You can either start from begining or resume from last session"
print "for resuming type in 'resume' else type in 'start'"
start=input()
if start=="resume":
    resume_file=open("project/ch.txt",'r')
    resume_ch=resume_file.read()
    resume_file.close()
    resume_file=open("project/i.txt",'r')
    resume_i=int(resume_file.read())
    resume_file.close()
for ch in alphabets:
    ch_file=open("project/ch.txt",'w')
    ch_file.write(ch)
    ch_file.close()
    if start=="resume":
        i=resume_i
    else:
        i=1
    if start=="resume":
        if ch==resume_ch:
            start="stop"
        if ch!=resume_ch:
            continue
    search_url="http://www.rottentomatoes.com/search/ajax/?searchtype=movie&search="+ch+"&page="+str(i)
    no_movies=0 
    while no_movies==0:
        search_page=urllib2.urlopen(search_url).read()
        search_soup=BeautifulSoup(search_page)
        for movie in search_soup.findAll('div',{"class":"media_block_content"}):
            if len(movie.findAll('ul'))==0:
                for m in movie.findAll('a'):
                    if str(m).find("_top")>=0:
                        movie_url="http://www.rottentomatoes.com/"+m.get('href')
                        movie_page=urllib2.urlopen(movie_url).read()
                        movie_soup=BeautifulSoup(movie_page)
                        links = []
                        title=movie_soup.findAll('title')
                        s=str(title).replace("<title>","")
                        s=s.replace("</title>","")
                        s=s.replace("Rotten Tomatoes","")
                        no_review=1
                        for link in movie_soup.findAll('a'):
                            if str(link).find(" all critic reviews")>0:
                                review_list_url="http://www.rottentomatoes.com"+link.get('href')
                                no_review=0
                                p=re.compile('\W')
                                st=re.sub(p,'',s)
                                pth1="project/corpus/positive"+st
                                pth2="project/corpus/negative"+st
                                if not os.path.exists(pth1):
                                    os.mkdir(path1)
                                    print title
                                if not os.path.exists(pth2):
                                    os.mkdir(path2)
                                
                        if no_review==1:
                            print "no reviews found!"+s+"skipped !"
        if len(search_soup.findAll('div',{"class":"media_block_content"}))==0:
            no_movies=1  
        i=i+1   
        i_file=open("project/i.txt",'w')  
        i_file.write(str(i))  
        i_file.close() 
        search_url="http://www.rottentomatoes.com/search/ajax/?searchtype=movie&search="+ch+"&page="+str(i)
       