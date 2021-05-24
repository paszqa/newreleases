from bs4 import BeautifulSoup
import requests
#import replace
import re




def saveCSV(siteurl,htmlname,csvname):
    ##Download website
    #url =  'https://www.gry-online.pl/daty-premier-gier.asp?PLA=1'
    r = requests.get(siteurl, allow_redirects=True)
    open(htmlname, 'wb').write(r.content)


    #Change data to csv
    html = open(htmlname, encoding="utf8", errors='ignore')
    soup = BeautifulSoup(html, 'html.parser')
    credits = soup.find_all("div", {"class" : "daty-premier-2017"})
    credits = re.sub(r'<a class="box"(.*)">\n', '', str(credits))
    credits = re.sub(r'<div>','', str(credits))
    credits = re.sub(r' <i>',';',credits)
    credits = re.sub(r'</i>','',credits)
    credits = re.sub(r'<div data-cnt(.*)">','', str(credits))
    credits = re.sub(r'</div>\n',';', str(credits))
    credits = re.sub(r';</a>','', credits)
    credits = re.sub(r'<div class="clr">;</div>]','',credits)
    credits = re.sub(r'\[<div class="daty-premier-2017">\n','', credits)
    credits = re.sub(r'<span(.*)</span>\n','', credits)
    credits = re.sub(r'\n</a>\n','',credits)
    credits = re.sub(r'\n</p>\n','',credits)
    credits = re.sub(r'</p>','',credits)
    credits = re.sub(r'<p (.*)>','',credits)
    print (credits)

    csv = open(csvname,'w')
    csv.write("Data;Nazwa;Platforma;Inne\n")
    csv.write(credits)
    csv.close()


saveCSV('https://www.gry-online.pl/daty-premier-gier.asp?PLA=1','new.html','new.csv')
saveCSV('https://www.gry-online.pl/daty-premier-gier.asp?PLA=1&CZA=2','month.html','month.csv')
saveCSV('https://www.gry-online.pl/daty-premier-gier.asp?PLA=1&CZA=3','6m.html','6m.csv')
#with open("https://www.gry-online.pl/daty-premier-gier.asp?PLA=1") as fp:
#    soup = BeautifulSoup(fp, 'lxml')

#soup = BeautifulSoup("<html>a web page</html>", 'lxml')
