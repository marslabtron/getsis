# encoding:utf-8
import urllib, urllib2, cookielib, re
#这是网址 http://38.103.161.187/bbs/index.php
# 填写账号信息
myname = ''
password = ''
 
cj = cookielib.CookieJar()
cookie_hanler = urllib2.HTTPCookieProcessor(cj)
 
lgurl = 'http://38.103.161.187/bbs/logging.php?action=login'
req = urllib2.Request(url = lgurl)
opener = urllib2.build_opener(cookie_hanler)
urllib2.install_opener(opener)
contents = opener.open(req)
contents = contents.read()

reg = r'<input type="hidden" name="formhash" value="(.*?)" />'
pattern = re.compile(reg)
result = pattern.findall(contents)
 
lgurl = 'http://38.103.161.187/bbs/logging.php?action=login'
formhash = result[0]
data = {'formhash':formhash, 'referer':'index.php', 'loginfield':'username','62838ebfea47071969cead9d87a2f1f7':myname, 'c95b1308bda0a3589f68f75d23b15938':password, 'questionid':0, 'cookietime':2592000, 'loginsubmit':'true'}
data = urllib.urlencode(data)
hdr = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0', 'Referer':'http://38.103.161.187/bbs/logging.php?action=login', 'Host':'38.103.161.187'}
req = urllib2.Request(url = lgurl, data = data, headers = hdr)
opener = urllib2.build_opener(cookie_hanler)

response = opener.open(req)
page = response.read()
#print(page)
 
contents = urllib2.urlopen('http://38.103.161.187/bbs/forumdisplay.php?fid=230&filter=type&typeid=1255')
contents = contents.read()
#print contents

tiezipattern=re.compile('<span id="thread\_.+?"><a href="viewthread\.php\?tid=(.*?)&amp\;extra=page\%3D1\%26amp\%3Bfilter\%3Dtype\%26amp\%3Btypeid\%3D1255" style="font-weight: bold;color: blue">')
tieziurl=re.findall(tiezipattern,contents)

myfile=open('number.ini','r')
b = myfile.readline()
b=int(b)
myfile.close

endurl=[]
for i in tieziurl:
    a=int(i)
    if a>b:
        endurl.append(i)
    else:
        pass

if endurl==[]:
    pass
else:
    print max(endurl)
    myfile=open('number.ini','w')
    myfile.write(max(endurl))
    myfile.close

for item in endurl:
    tzurl= 'http://38.103.161.187/bbs/' +'viewthread.php?tid=' + item + '&amp;extra=page%3D1%26amp%3Bfilter%3Dtype%26amp%3Btypeid%3D1255'
    contents = urllib2.urlopen(tzurl)
    contents = contents.read()
    tpattern = re.compile('<a href="(attachment\.php\?aid=.*?)" target="\_blank">')
    torrent = re.findall(tpattern, contents)
    tail= torrent[0]
    code=tail[19:26]
    print tail
    turl = 'http://38.103.161.187/bbs/' + tail
    urllib.urlretrieve(turl, '%s.torrent' % (code))
    print 'Downloading %s is done.' % (code)
