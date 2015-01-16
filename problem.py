#! /usr/local/bin/python
import urllib2
import BeautifulSoup
from BeautifulSoup import BeautifulSoup
import re
import os
import socket

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
    #loop for navigating through all search pages, searching a to z
    ch_file=open("project/ch.txt",'w')
    ch_file.write(ch)
    ch_file.close()
    if start=="resume":
        i=resume_i
    else:
        i=1
    if start=="resume":
        if ch!=resume_ch:
            continue
    search_url="http://www.rottentomatoes.com/search/ajax/?searchtype=movie&search="+ch+"&page="+str(i)
    no_movies=0 
    while no_movies==0:
        #loop for navigating through different pages in an alphabet search
        search_page=urllib2.urlopen(search_url).read()
        search_soup=BeautifulSoup(search_page)
        mov_n=1
        mov_total=0
        print "movie number intialised to one"
        for movie in search_soup.findAll('div',{"class":"media_block_content"}):
            if len(movie.findAll('ul'))==0:
                mov_total=mov_total+1

        for movie in search_soup.findAll('div',{"class":"media_block_content"}):
            if len(movie.findAll('ul'))==0:
                if start=="resume":
                    resume_file=open("project/mov.txt",'r')
                    resume_mov_n=int(resume_file.read())
                    resume_file.close()
                    if mov_n==resume_mov_n:
                        start="stop"
                        print "resumed"
                    if mov_n!=resume_mov_n:
                        mov_n=mov_n+1
                        print "one movie skipped"+str(mov_n)
                        continue

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

                        #finds the link to the review list page
                         
                            if str(link).find(" all critic reviews")>0:
                                review_list_url="http://www.rottentomatoes.com"+link.get('href')
                                no_review=0
                                p=re.compile('\W')  #This removes all the non alphabets
                                st=re.sub(p,'',s)   #from the srting 's'

                                pth1="project/corpus/positive/"+st
                                pth2="project/corpus/negative/"+st

                                if not os.path.exists(pth1):
                                    os.mkdir(pth1)
                                    print title
                                if not os.path.exists(pth2):
                                    os.mkdir(pth2)

                                def scrap_review(page,nm,path):
                                    #scraps the review alone from the review site
                                    
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

                                    for j in range(len(review)):
                                        review[j]=review[j].replace("&#8217;","'")
                                        review[j]=review[j].replace("&#8220;","'")
                                        review[j]=review[j].replace("&#8221;","'")
                                        review[j]=review[j].replace("&#8230;","...")
                                        review[j]=review[j].replace("&#39;","'")
                                        review[j]=review[j].replace("&#039;","'")
                                        review[j]=review[j].replace("&#34;","'")
                                        review[j]=review[j].replace("&#034;","'")
                                        review[j]=review[j].replace("&ldquo;","'")
                                        review[j]=review[j].replace("&lsquo;","'")
                                        review[j]=review[j].replace("&rdquo;","'")
                                        review[j]=review[j].replace("&rsquo;","'")
                                        review[j]=review[j].replace("&#146;","'")
                                        review[j]=review[j].replace("&quot;","'")
                                        review[j]=review[j].replace("&#147;","'")
                                        review[j]=review[j].replace("&#148;","'")
                                        review[j]=review[j].replace("&nbsp;","")
                                        review[j]=review[j].replace("&amp;","&")
                                        review[j]=review[j].replace("&apos;","'")



        
                                    myfile=open(path+"/review"+str(nm)+".txt",'w')
                                    for text in review:
                                        myfile.write(text)

                                    myfile.close()

                               
                                #req=urllib2.Request(review_list_url,headers={'User-agent:','Mozilla/5.0'})
                                n=1 
                                #tracks number of negative reviews
                                p=1
                                #tracks number of positive reviews
                                flag=1

                                while flag==1:
                                # loop for navigating through the review list pages
    
                                    review_list_page=urllib2.urlopen(review_list_url)
                                    review_list_soup=BeautifulSoup(review_list_page)

                                    for div in review_list_soup.findAll('div',{"class":"media_block_content"}):
                                        for div2 in div.findAll('div'):
                                            for rating in div2.findAll('div'):
                                                if str(rating).find("small rotten")>0:
                                                    for review in div.findAll('a'):
                                                        if str(review).find("Full Review")>0:
                                                            review_url=review.get("href")
                                                            try:
                                                                review_page=urllib2.urlopen(review_url,timeout=10).read()
                                                            except urllib2.URLError:
                                                                print "BAD URL"
                                                                continue
                                                            except socket.timeout:
                                                                print "timeout"
                                                                continue
                                                            except ValueError:
                                                                print "value error"
                                                                continue
                                                            except socket.error:
                                                                print "error"
                                                                continue
                                                            except urllib2.HTTPError:
                                                                print "http error"
                                                                continue
                                                            scrap_review(review_page,n,pth2)
                                                            print "review" + str(n+p-1)
                                                            n=n+1

                                                elif str(rating).find("small fresh")>0:
                                                    for review in div.findAll('a'):
                                                        if str(review).find("Full Review")>0:
                                                            review_url=review.get("href")
                                                            try:
                                                                review_page=urllib2.urlopen(review_url,timeout=10).read()
                                                            except urllib2.URLError:
                                                                print "BAD URL"
                                                                continue
                                                            except socket.timeout:
                                                                print "timeout"
                                                                continue
                                                            except ValueError:
                                                                print "value error"
                                                                continue
                                                            except socket.error:
                                                                print "error"
                                                                continue
                                                            except urllib2.HTTPError:
                                                                print "http error"
                                                                continue
                                                            scrap_review(review_page,p,pth1)
                                                            print "review" + str(n+p-1)
                                                            p=p+1
                            



                                    for link in review_list_soup.findAll('a'): #navigates to the next page
                                        if str(link).find("button pagination right")>0:
                                            review_list_url="http://www.rottentomatoes.com"+link.get('href')
                                            flag=1
                                            break
                                            

                                        else:
                                             flag=0 


                        if no_review==1:
                            print "no reviews found!"+s+"skipped !"

                if mov_n==mov_total:
                    mov_n=1
                else:
                    mov_n=mov_n+1
                print "mov no incremeneted to "+str(mov_n)
                mov_file=open("project/mov.txt",'w')
                mov_file.write(str(mov_n))
                mov_file.close()

        if len(search_soup.findAll('div',{"class":"media_block_content"}))==0:
            no_movies=1  
           
        i=i+1
        i_file=open("project/i.txt",'w')  
        i_file.write(str(i))  
        i_file.close() 
        search_url="http://www.rottentomatoes.com/search/ajax/?searchtype=movie&search="+ch+"&page="+str(i)
       