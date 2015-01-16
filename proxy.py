import urllib2
proxy_url="http://balagopal:25031993@netmon.iitb.ac.in:80"
proxy_support=urllib2.ProxyHandler({'http':proxy_url})
opener=urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)
opener.addheaders=[('User-agent','Mozilla/21.0')]
