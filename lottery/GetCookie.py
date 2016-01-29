import cookielib
import urllib2

filename = 'cookie1.txt'
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open("http://baidu.lecai.com")
cookie.save(ignore_discard=True, ignore_expires=True)