import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

index = 30

URL_TEMPLATE = "https://new.spbkap.ru/applications/numbers"
r = requests.get(URL_TEMPLATE)
soup = bs(r.text, "html.parser")
parsed = soup.find_all('td')
spis = []

for name in parsed:
    m = re.search(r'<td style="text-align: center; vertical-align: middle;">(.*?)</td>', str(name)) 
    if m: 
        found = m.group(1) 
    else: 
        found = None 

    if found == None:
        c = re.search(r'<td style="vertical-align: middle;">(.*?)</td>', str(name)) 
        if c: 
            found = c.group(1) 
        else: 
            found = None
    
    if found == None:
        b = re.search(r'<td style="text-align: left; vertical-align: middle;">(.*?)</td>', str(name)) 
        if b: 
            found = b.group(1) 
        else: 
            found = None 

    if found!=None and len(str(found))<100:
        spis.append(str(found))
spis.pop(60)
spis.pop(88)
vacancy = ""
vacancies = []
index = 0
for i in range(len(spis)//4):
    for v in range(4):
        if v == 2 or v == 0:
            vacancy+=f"{spis[index]}. "
        elif v == 1:
            vacancy+=f"{spis[index]} "
        else:
            vacancy+=f"{spis[index]}"
        index+=1
    vacancies.append(vacancy)
    vacancy = ""
#print(vacancies)
nkl = vacancies[0:15]
ekl = vacancies[15:22]
""" x=3
print(nkl[x].split(". ")[3]) """
""" print(nkl)
print(ekl) """
