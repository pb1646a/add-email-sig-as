import os
from bs4 import BeautifulSoup
import re
import io
curr_path = os.path.dirname(os.path.realpath(__file__))
path1 = os.path.relpath('../../../email_signatures', curr_path)
files=[]
for r,d,f in os.walk(path1):
    for file in f:
        if '.html' in file:
            files.append(os.path.join(r,file))
files.sort()
count = 0
for html in files:
    path = os.path.relpath(html, curr_path)
    name = ''
    with io.open(path,'r+') as signature:
        count = count + 1
        content = signature.read()
        soup = BeautifulSoup(content,'lxml')
        link_el = soup.select_one("a[href*=mailto]")
        updated_filename = link_el.text + '.html'
        os.rename(html, os.path.join(path1, updated_filename))

        
