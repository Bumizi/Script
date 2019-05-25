import os
import sys
#import urllib.request
from urllib.parse import urlencode, quote_plus
from urllib.request import Request, urlopen
from xml.dom.minidom import parseString
def makeUrl_SearchByArea(sido, gugun):
    #client_id = "J0xlzLY_mwqXVGY7OBho"
    #encText = urllib.parse.quote("한국산업기술대")
    url = "http://www.culture.go.kr/openapi/rest/publicperformancedisplays/area"# + encText
    ServiceKey = '5jJOAyIYEGAq71RHF1AMCi8%2F0s%2Fw0G9%2FWlxzhjXUpSNItx2%2FeaCs9kruHWarDxWgAZOTCXtbeuVXbupzdqDm%2FQ%3D%3D'
    queryParams = '?' + 'serviceKey=' + ServiceKey + '&' + urlencode({quote_plus('sido'): sido, quote_plus('gugun'): gugun})
    return url + queryParams

def getApi_SearchByArea(sido, gugun):
    url = makeUrl_SearchByArea(sido, gugun)
    print (url)
    request = Request(url)
    response_body = urlopen(request).read()
    print(extractData_SearchByArea(response_body))
    return extractData_SearchByArea(response_body)

def extractData_SearchByArea(strXml):
    dom = parseString(strXml)
    strXml = dom
    SearchByArea = strXml.childNodes
    response = SearchByArea[0].childNodes
    body = response[1].childNodes
    items = body[5].childNodes
    for item in items:
        #data = item.childNodes
        #for element in data:
            if item.nodeName == "title":
                title = item.firstChild.data
            elif item.nodeName == "startDate":
                startDate = item.firstChild.data
            elif item.nodeName == "endDate":
                endDate = item.firstChild.data
            elif item.nodeName == "place":
                place = item.firstChild.data
            elif item.nodeName == "realmName":
                realmName = item.firstChild.data
            elif item.nodeName == "area":
                area = item.firstChild.data
            elif item.nodeName == "gpsX":
                gpsX = item.firstChild.data
            elif item.nodeName == "gpsY":
                gpsY = item.firstChild.data
    return {"title":title, "startDate":startDate, "endDate":endDate, "place":place,
            "realmName":realmName, "area":area, "gpsX":gpsX, "gpsY":gpsY}



def printMenu():
    print("\nWelcome! Book Manager Program (xml version)")
    print("========Menu==========")
    print("Load xml:  l")
    print("Quit program:   q")
    print("print Book list: b")
    print("----------------------------------------")
    print("========Menu==========")


def launcherFunction(menu):
    if menu == 'l':
        #LoadXMLFromFile()
        pass
    elif menu == 'q':
        QuitBookMgr()
    elif menu == 'b':
        #PrintBookList(["title", ])
        sido = str(input('시/도 입력 :'))
        gugun = str(input('구/군 입력 :'))
        getApi_SearchByArea(sido, gugun)
    else:
        print("error : unknown menu key")


def QuitBookMgr():
    global loopFlag
    loopFlag = 0

loopFlag = 1

##### run #####
while (loopFlag > 0):
    printMenu()
    menuKey = str(input('select menu :'))
    launcherFunction(menuKey)
else:
    print("Thank you! Good Bye")