#!/usr/bin/python
import urlparse
import urllib 

book_pages = ['pages/6dda7650725302f59ea42047206bd4ee5f928d19/GreatBookPage1.pdf','pages/aa814d1c25455480942cb4106e6cde84be86fb30/GreatBookPage2.pdf','pages/57737da397cbfda84e88b573cd96d45fcf34a5da/GreatBookPage3.pdf','pages/f192a884f68af24ae55d9d9ad4adf8d3a3995258/GreatBookPage4.pdf','pages/05c0cacc8cfb96bb5531540e9b2b839a0604225f/GreatBookPage5.pdf','pages/8943e0524e1bf0ea8c7968e85b2444323cb237af/GreatBookPage6.pdf','pages/c1df4dbc96a58b48a9f235a1ca89352f865af8b8/GreatBookPage7.pdf']
for i in xrange(len(book_pages)):
    url = 'https://www.holidayhackchallenge.com/2017/{}'.format(book_pages[i])
    urlparts = urlparse.urlsplit(url)
    filename = urlparts.path.split('/')[-1]
    print '\n[*]Downloading %s' % filename
    
    testfile = urllib.URLopener()
    testfile.retrieve(url, filename)

