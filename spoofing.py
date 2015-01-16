opener=urllib2.build_opener()
opener.addheaders=[('User-agent','Mozilla/5.0')]
urllib2.install_opener(opener)