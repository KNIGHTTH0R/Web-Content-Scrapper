Web Content Scrapper 
====================

The scapper works on the site "www.rottentomatoes.com". It crawls through all
the movies in the site and the review urls listed under each movie. It then
scraps the review alone from the review site. Acording to the positive or 
negative tag given by the rottentomatoes site, the scrapped review is saved 
as a text in file in 'corpus/positive/movie_name' or 'corpus/negative/movie_name'
accordingly.


Dependencies
------------

1. Python 2.7.x

2. BeautifulSoup Package


To Start With
-------------

1. If proxy is needed for the internet connection, open the file proxy.py
   in a text editor and add the username, password and the gateway.
2. Run proxy.py in python.
   Code for executing a file is execfile(path)
3. Run project.py in python
4. When prompted type in "start" with the quotes.
   Incase you had run the program before and stopped it in between, you 
   can resume from the last movie. For that type in "resume" with quotes.


Summary
-------

The program searches each alphabet (ch) in the given site and from each searche,
it navigates through the result pages that are numbered 1,2...(i) . Two loops 
are kept for this purpose. From those pages program moves to each movie page 
and from it to the page if review site list. From the respective movie site, the
review alone is then scrapped. Depending on the positive or negative rating given
scrapped review is stored as text files in different folders.


Functions
---------

scrap_review(page,nm,path)

The arguments are page, nm and path. Page is string containing html code of the 
review page. nm is the review number. The name of text file to which review is 
stored will be as 'reviewnm'. Path is the directory path, where review is to be
stored. It depends on the rating negative or positive.

visible(element)

Visible returns false if the argument element(an html entity) is a style,head,
document,script or title. Else it returns true. It is used to find the visible 
part alone from the review page. From the visible part, the review part alone is
extracted by checking the len of each element.


Appendix
--------

urllib2.urlopen(url).read() : reads the page specified by url and returns html
			      code as string.

BeautifulSoup(page) : converts the html code into BeautifulSoup format. It is 
		      easy to find tags and manage html in this format.

BeautifulSoup(page).findALL('tag'): Returns an array of all tags named 'tag' in 
				    html code.
