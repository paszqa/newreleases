#Count execution time
from datetime import datetime
startTime = datetime.now()

#Imports
import os
import sys
from PIL import Image, ImageDraw, ImageFont

#Choose size and color
#img = Image.new('RGB', (550, 400), color = (73, 109, 137))
img = Image.open('/home/pi/newreleases/background.png')
img = img.convert("RGB")
#Choose fonts
pathToScript='/home/pi/newreleases/'
largefnt = ImageFont.truetype(pathToScript+'ShareTechMono-Regular.ttf', 18)
fnt = ImageFont.truetype(pathToScript+'ShareTechMono-Regular.ttf', 13)
smallfnt = ImageFont.truetype(pathToScript+'ShareTechMono-Regular.ttf',11)
#Settings
rowHeight=14
firstRowStart=18

#Draw background
d = ImageDraw.Draw(img,'RGBA')

#Get text from file
which=sys.argv[1]
if which == "month":
    filename = "month-eng.png"
    titletext = "Games releasing soon"
    f = open(pathToScript+'month-eng.csv','r')
    indent = 160
elif which == "6m":
    filename = "6m-end.png"
    f = open(pathToScript+'6m-eng.csv','r')
    titletext = "Games releasing within 6 months"
    indent = 130
else:
    filename = "new-eng.png"
    f = open(pathToScript+'new-eng.csv','r')
    titletext = "Fresh releases"
    indent = 170


#Analyze each line from the file
rowNumber = 0
for row in f:
    if rowNumber > 25:
        break;
    rowSplit = row.split(";")
    if rowNumber == 0:
        currentColor = (122,122,122) #grey
    elif rowNumber > 0 and rowNumber < 5:
        currentColor = (49, 199, 38) #green
    elif rowNumber > 4 and rowNumber < 8:
        currentColor = (169, 199, 38) #light green
    elif rowNumber > 7 and rowNumber < 12:
        currentColor = (199, 194, 38) # yellowish
    else:
        currentColor = (199, 140, 38) #orange
    d.text((10,firstRowStart+rowHeight*rowNumber), rowSplit[0], font=fnt, fill=currentColor)
    if rowNumber % 2:
        d.rectangle([(0,(firstRowStart+rowHeight*rowNumber)+2),(530,firstRowStart+rowHeight*(rowNumber+1)+1)], fill=(0,0,0,57))
    d.text((100,firstRowStart+rowHeight*rowNumber), rowSplit[1][0:45], font=fnt, fill=currentColor)
    d.text((450,firstRowStart+rowHeight*rowNumber), rowSplit[2], font=fnt, fill=currentColor)
#    d.text((470+min(1,rowNumber)*15,firstRowStart+rowHeight*rowNumber), rowSplit[3], font=fnt, fill=currentColor)
    rowNumber += 1

#Add title
d.text((indent,3), titletext, font=largefnt, fill=(255,255,255))

#Add execution time info
executionTime=str(round(datetime.now().timestamp() - startTime.timestamp(),2))
print("EX:"+executionTime+" NOW:"+str(datetime.now()))
d.text((0,390), "Generated in ~"+str(executionTime)+" seconds by qBot on "+str(datetime.now())[0:-7]+". Long live Slav Squat Squad!", font=smallfnt, fill=(20,20,20))
#Save for the glory of Slav Squat Squad
img.save(pathToScript+filename)
