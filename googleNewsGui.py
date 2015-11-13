from tkinter import *
from tkinter import ttk
import urllib
import urllib.request
from newspaper import Article
from fake_useragent import UserAgent
from bs4 import BeautifulSoup 
import re
import time
import nltk
from nltk import sent_tokenize, word_tokenize
import datetime
from datetime import datetime, timedelta
# self defined
from googleCrawlerPython3 import googleNews


def _search():
    t.grid(column=0,row=5,columnspan=4,pady=15)
    # get entry content
    entryContent = name.get()
    entryContent = re.sub(" ", "", entryContent)
    commaIndex = entryContent.index(',')
    term = entryContent[0:commaIndex]
    pageNum = entryContent[commaIndex + 1:]
    print(term)
    print(pageNum)
    prPageNum = pageNum
    pageNum = int(pageNum)
    news = googleNews(pageNum, term)
    t.insert("1.0", "Crawling finished\n\n")
    t.insert("2.0", "Search term is " + term + "\n\n")
    t.insert("3.0", "Search page number is " + prPageNum + "\n\n")
    t.insert("4.0", "News is stored in the same directory with the programms\n\n")

def _analyzeInput():
    entryContent = name.get()

root = Tk()
root.resizable(FALSE, FALSE)
root.title('google news crawler')
root.geometry('+800+400')
content = ttk.Frame(root, padding=(20, 3, 20, 3))
image = PhotoImage(file='utdallas.gif')
Labelurl = ttk.Label(content)
Labelurl['image']=image

#---label---
lf = ttk.Labelframe(content, text='type in what to search')
namelbl = ttk.Label(lf, text="key word, page: ")
url=StringVar()
name = ttk.Entry(lf,textvariable=url)
example = ttk.Label(lf, text="ex: china, 10")
parse = ttk.Entry(content, width = 4)

#---button---
p = ttk.Progressbar(content, orient=HORIZONTAL, length=380, mode='indeterminate')
ok = ttk.Button(content, text="search", command=_search, width=8)
t = Text(content, width=56, height=20, yscrollcommand='yview')

#---grid---
content.grid(column=0, row=0,sticky=(N, S, E, W))
Labelurl.grid(column=0, row=0,columnspan=4, rowspan=1,pady=5,padx=3)
lf.grid(column=0, row=1,columnspan=4,sticky=(N, S, E, W), rowspan=1,pady=10,padx=3)
# grid label
namelbl.grid(column=0, row=0)
name.grid(column=1, row=0,columnspan=2,rowspan=1)
example.grid(column=3, row=0)
# grid button
ok.grid(column=4, row=2, pady=5,padx=3)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=1)
content.columnconfigure(1, weight=1)
content.columnconfigure(2, weight=1)
content.columnconfigure(3, weight=1)
content.rowconfigure(1, weight=1)

root.mainloop()

