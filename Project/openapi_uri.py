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
    return extractData_SearchByArea(response_body)

def extractData_SearchByArea(strXml):
    dom = parseString(strXml)
    strXml = dom
    SearchByArea = strXml.childNodes
    response = SearchByArea[0].childNodes
    body = response[1].childNodes
    items = body[0].childNodes
    for item in items:
        data = item.childNodes
        for element in data:
            if element.nodeName == "sido":
                sido = element.firstChild.nodeValue
            elif element.nodeName == "gugun":
                gugun = element.firstChild.nodeValue
            elif element.nodeName == "perforList":
                for element in data:
                    if element.nodeName == "title":
                        title = element.firstChild.nodeValue
                    elif element.nodeName == "startDate":
                        startDate = element.firstChild.nodeValue
                    elif element.nodeName == "endDate":
                        endDate = element.firstChild.nodeValue
                    elif element.nodeName == "place":
                        place = element.firstChild.nodeValue
                    elif element.nodeName == "realmName":
                        realmName = element.firstChild.nodeValue
                    elif element.nodeName == "area":
                        area = element.firstChild.nodeValue
                    elif element.nodeName == "gpsX":
                        gpsX = element.firstChild.nodeValue
                    elif element.nodeName == "gpsY":
                        gpsY = element.firstChild.nodeValue

    return {"sido":sido, "gugun":gugun, "title":title, "startDate":startDate, "endDate":endDate, "place":place,
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