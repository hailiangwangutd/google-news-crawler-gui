# Title: Google News Crawler
# Time: July 31, 2015
# Description: Download by date, smaller number, more recently date.
# To modify how many pages to download, change second parameter 
# in 'range function', '5' as the fifth page in google news search 
# result. To modify what to search, change 'term' parameter.
# Every document is a single news, with news source, news time, news 
# contents included.
# Note: You may install packages included first to use this program.

import urllib
import urllib.request
from bs4 import BeautifulSoup 
import re
import time
from newspaper import Article
from fake_useragent import UserAgent
import nltk
from nltk import sent_tokenize, word_tokenize
import datetime
from datetime import datetime, timedelta

class googleNews:
    
    def __init__(self, pageNum, term):
        
        def getGoogleNewsLinks(subsite, artNum, term):
                time.sleep(15)
                url = "http://www.google.com/search?q=" + term + "&tbs=sbd:1&tbm=nws&start=" + subsite
                req = urllib.request.Request(url, headers=headers)
                resp = urllib.request.urlopen(req)
                soup = BeautifulSoup(resp, "lxml")
                links = soup.findAll('div', attrs={'id': 'search'})
                regex = "q=.*&sa"
                pattern = re.compile(regex)
                artTitle = []
                if(links != []):
                        links = links[0]
                        links = links.findAll('li', attrs={'class':'g'})
                        for l in links:
                                time0 = l.findAll('span', attrs={'class':'f'})[0]
                                time0 = time0.contents[0].strip()
                                time1 = time0
                                l = l.find('a')
                                if(l != []):
                                        l = l.get('href')
                                        l = str(l)
                                        l = re.findall(pattern, l)
                                        if(l != []):
                                                l = l[0][2:-3]
                                                linkSet.append(l)
                                                artNum = str(artNum)
                                                getNewsContents(l, artNum, artTitle, time0, time1)
                                                artNum = int(artNum)
                                                artNum += 1

        def getNewsContents(url, artNum, artTitle, time0, time1):
            try:
                    a = Article(url, language='en')
                    a.download()
                    a.parse()
                    print(a.title)
                    fo = open(artNum, "wb")
                    time0 = getFormalTime(time0)
                    if(time0 != None):
                            fo.write(time0.encode('utf-8'))
                            print("****"+time0+"****")
                    else:
                            fo.write(time1.encode('utf-8'))
                            print("****"+time1+"****")
                    fo.write(". ".encode('utf-8'))
                    fo.write(a.title.encode('utf-8'))
                    fo.write(". \n\n".encode('utf-8'))
                    fo.write(a.text.encode('utf-8'))
                    fo.close()
                    artTitle.append(a.title)
            except Exception as e:
                print(str(e))

        def getFormalTime(time0):
            word = word_tokenize(time0)
            replace = ""
            timeIndex = ""
            preIndex = ""
            for x in word:
                if(x == "minute" or x == "hour" or x == "day"
                   or x == "minutes" or x == "hours" or x == "days"):
                    timeIndex = word.index(x)
                    preIndex =  timeIndex - 1
                    actualTime = [word[preIndex],word[timeIndex]]
                    if(actualTime != []):
                        formalTime = formalizeTime(actualTime)
                        replace = " - " + actualTime[0] + " " +actualTime[1] + " ago"
                        if(replace != " -   ago."):
                            formalTime = " - " + formalTime
                            time0 = re.sub(replace, formalTime, time0)
                            return time0

        def formalizeTime(actualTime):
            relativeTime = int(actualTime[0])
            clock = ""
            if(actualTime[1] == 'minute' or actualTime[1] == 'minutes'):
                lastMinuteDateTime = datetime.today() - timedelta(minutes = relativeTime)
                return(lastMinuteDateTime.strftime('%Y-%m-%d %H:%M:%S'))
            if(actualTime[1] == 'hour' or actualTime[1] == 'hours'):
                lastHourDateTime = datetime.today() - timedelta(hours = relativeTime)
                return(lastHourDateTime.strftime('%Y-%m-%d %H:%M:%S'))
            if(actualTime[1] == 'day' or actualTime[1] == 'days'):
                lastHourDateTime = datetime.today() - timedelta(days = relativeTime)
                return(lastHourDateTime.strftime('%Y-%m-%d %H:%M:%S'))

        ua = UserAgent()
        headers = {'User-agent': 'foobar'}
        artNum = 1
        linkSet = []
        self.pageNum = pageNum;
        self.term = term;
        print("Begin")
        for i in range(0, pageNum):
                pageNum = str(i*10)
                getGoogleNewsLinks(pageNum, artNum, term)
                artNum += 10
        print(len(linkSet))



