from bs4 import BeautifulSoup
import requests
#import replace
import re



###########################################################
#
# GET SITE, SAVE AS HTML, GENERATE SIMPLE CSV
#
###########################################################

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
    csv.write("Date;Name;Genre;Platform;Other\n")
    csv.write(credits)
    csv.close()


saveCSV('https://www.gry-online.pl/daty-premier-gier.asp?PLA=1','new.html','new.csv')
saveCSV('https://www.gry-online.pl/daty-premier-gier.asp?PLA=1&CZA=2','month.html','month.csv')
saveCSV('https://www.gry-online.pl/daty-premier-gier.asp?PLA=1&CZA=3','6m.html','6m.csv')

##############################################################
#
# GENERATE SHORT TRANSLATED FILE
#
##############################################################

def translate(sourcecsv,outputcsv):
    f = open(outputcsv,'w')
    with open(sourcecsv) as file:
        array = file.readlines()
        for line in array[1:15]:
            lineSplit = line.split(';')
            # Date transform
            dateSplit = lineSplit[0].split(' ')
            dateFinal = ""
            if len(dateSplit) > 1:
                if len(dateSplit) > 2:
                    dateFinal += dateSplit[0] + " ";

                if "sty" in dateSplit[-2]:
                    dateFinal += "Jan"
                elif "lut" in dateSplit[-2]:
                    dateFinal += "Feb"
                elif "mar" in dateSplit[-2]:
                    dateFinal += "Mar"
                elif "kwi" in dateSplit[-2]:
                    dateFinal += "Apr"
                elif "maj" in dateSplit[-2]:
                    dateFinal += "May"
                elif "czer" in dateSplit[-2]:
                    dateFinal += "Jun"
                elif "lipi" in dateSplit[-2]:
                    dateFinal += "Jul"
                elif "sier" in dateSplit[-2]:
                    dateFinal += "Aug"
                elif "wrze" in dateSplit[-2]:
                    dateFinal += "Sep"
                elif "ernik" in dateSplit[-2]:
                    dateFinal += "Oct"
                elif "list" in dateSplit[-2]:
                    dateFinal += "Nov"
                elif "grud" in dateSplit[-2]:
                    dateFinal += "Dec"
                dateFinal += " "+dateSplit[-1]
            else:
                dateFinal = dateSplit[-1]
            #
            # Genre transform
            genre = lineSplit[2];
            if "Zrcz" in genre:
                genre = "Action"
            elif "Fabul" in genre:
                genre = "RPG"
            elif "Symu" in genre:
                genre = "Sim"
            elif "Wyci" in genre:
                genre = "Racing"
            elif "Akcj" in genre:
                genre = "Action"
            elif "Przyg" in genre:
                genre = "Adventure"
            elif "Strat" in genre:
                genre = "Strategy"

            # Write to file
            f.write(dateFinal+";"+lineSplit[1]+";"+genre+"\n")
            print(dateFinal+";"+lineSplit[1]+";"+genre)
    print("=================================================")
    f.close()
translate('new.csv','new-eng.csv')
translate('month.csv','month-eng.csv')
translate('6m.csv','6m-eng.csv')


