import requests
from bs4 import BeautifulSoup
url ="https://codewithharry.com"
r=requests.get(url)
htmlContent=r.content
#p rint(htmlContent)
soup=BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify)
title=soup.title
# print(title)
# four type of object in bs
# 1.tag
# 2.navigation string
# 3.beautifuksoup
# 4.comments
""" print(type(title))
print(type(soup))
print(type(title.string)) """
paras=soup.find_all('p')
""" print(paras) """
anchor=soup.find_all('a')
""" print(anchor) """
""" print(soup.find('p')) """
""" print(soup.find('p')['class']) """
""" for link in anchor:
    print(link.get('href')); """
for link in anchor:
    if(link !='#'):
        link="https://codewithharry.com"+link.get('href')
        #all_links.add(link)
        #print(link)
        # comment
        markup="<p><!--this is a comment..></p>"
        soup2=BeautifulSoup(markup )
       # print(soup2.p)
        #exit()
#print(soup2.p.string)
print(type(soup2.string))
exit()
ncp=soup.find('')