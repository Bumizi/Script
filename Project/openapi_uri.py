import os
import sys
#import urllib.request
from urllib.parse import urlencode, quote_plus
from urllib.request import Request, urlopen
from xml.dom.minidom import parseString

DataList = []

# 지역별 검색
def makeUrl_SearchByArea(sido, gugun, rows):
    #client_id = "J0xlzLY_mwqXVGY7OBho"
    #encText = urllib.parse.quote("한국산업기술대")
    url = "http://www.culture.go.kr/openapi/rest/publicperformancedisplays/area"# + encText
    ServiceKey = '5jJOAyIYEGAq71RHF1AMCi8%2F0s%2Fw0G9%2FWlxzhjXUpSNItx2%2FeaCs9kruHWarDxWgAZOTCXtbeuVXbupzdqDm%2FQ%3D%3D'
    queryParams = '?' + 'serviceKey=' + ServiceKey + '&' + urlencode({quote_plus('sido'): sido, quote_plus('gugun'): gugun, quote_plus('rows'): rows})
    return url + queryParams

def getApi_SearchByArea(sido, gugun, rows):
    url = makeUrl_SearchByArea(sido, gugun, rows)
    print (url)
    request = Request(url)
    response_body = urlopen(request).read()
    print(extractData_PerforList(response_body))
    return extractData_PerforList(response_body)



# 기간별 검색
def makeUrl_SearchByPeriod(start, end, rows):
    #client_id = "J0xlzLY_mwqXVGY7OBho"
    #encText = urllib.parse.quote("한국산업기술대")
    url = "http://www.culture.go.kr/openapi/rest/publicperformancedisplays/period"# + encText
    ServiceKey = '5jJOAyIYEGAq71RHF1AMCi8%2F0s%2Fw0G9%2FWlxzhjXUpSNItx2%2FeaCs9kruHWarDxWgAZOTCXtbeuVXbupzdqDm%2FQ%3D%3D'
    queryParams = '?' + 'serviceKey=' + ServiceKey + '&' + urlencode({quote_plus('from'): start, quote_plus('to'): end, quote_plus('rows'): rows})
    return url + queryParams

def getApi_SearchByPeriod(start, end, rows):
    url = makeUrl_SearchByPeriod(start, end, rows)
    print (url)
    request = Request(url)
    response_body = urlopen(request).read()
    print(extractData_PerforList(response_body))
    return extractData_PerforList(response_body)



# 분야별 검색
def makeUrl_SearchByRealm(realm, rows):
    #client_id = "J0xlzLY_mwqXVGY7OBho"
    #encText = urllib.parse.quote("한국산업기술대")
    url = "http://www.culture.go.kr/openapi/rest/publicperformancedisplays/realm"# + encText
    ServiceKey = '5jJOAyIYEGAq71RHF1AMCi8%2F0s%2Fw0G9%2FWlxzhjXUpSNItx2%2FeaCs9kruHWarDxWgAZOTCXtbeuVXbupzdqDm%2FQ%3D%3D'
    if realm == "연극":
        realmCode = "A000"
    elif realm == "음악":
        realmCode = "B000"
    elif realm == "무용":
        realmCode = "C000"
    elif realm == "미술":
        realmCode = "D000"
    elif realm == "건축":
        realmCode = "E000"
    elif realm == "영상":
        realmCode = "G000"
    elif realm == "문학":
        realmCode = "H000"
    elif realm == "문화정책":
        realmCode = "I000"
    elif realm == "축제문화공간":
        realmCode = "J000"
    elif realm == "기타":
        realmCode = "L000"
    queryParams = '?' + 'serviceKey=' + ServiceKey + '&' + urlencode({quote_plus('realmCode'): realmCode, quote_plus('rows'): rows})
    return url + queryParams

def getApi_SearchByRealm(realm, rows):
    url = makeUrl_SearchByRealm(realm, rows)
    print (url)
    request = Request(url)
    response_body = urlopen(request).read()
    print(extractData_PerforList(response_body))
    return extractData_PerforList(response_body)



# 상세 검색
def makeUrl_SearchBySeq(seq):
    #client_id = "J0xlzLY_mwqXVGY7OBho"
    #encText = urllib.parse.quote("한국산업기술대")
    url = "http://www.culture.go.kr/openapi/rest/publicperformancedisplays/d/"# + encText
    ServiceKey = '5jJOAyIYEGAq71RHF1AMCi8%2F0s%2Fw0G9%2FWlxzhjXUpSNItx2%2FeaCs9kruHWarDxWgAZOTCXtbeuVXbupzdqDm%2FQ%3D%3D'
    queryParams = '?' + 'serviceKey=' + ServiceKey + '&' + urlencode({quote_plus('seq'): seq})
    return url + queryParams

def getApi_SearchBySeq(seq):
    url = makeUrl_SearchBySeq(seq)
    print (url)
    request = Request(url)
    response_body = urlopen(request).read()
    print(extractData_SpecificPerfor(response_body))
    #print(spam.strlen(url))
    return extractData_SpecificPerfor(response_body)



# 데이터 추출
def extractData_PerforList(strXml):
    global DataList
    DataList.clear()
    dom = parseString(strXml)
    strXml = dom
    PerforList = strXml.childNodes
    response = PerforList[0].childNodes
    body = response[1].childNodes
    for items in body:
        if items.nodeName == "perforList":
            for item in items.childNodes:
                if item.nodeName == "seq":
                    seq = item.firstChild.data
                elif item.nodeName == "title":
                    title = item.firstChild.data
                elif item.nodeName == "startDate":
                    if item.firstChild is not None:
                        startDate = item.firstChild.data
                    else:
                        startDate = "정보없음"
                elif item.nodeName == "endDate":
                    if item.firstChild is not None:
                        endDate = item.firstChild.data
                    else:
                        endDate = "정보없음"
                elif item.nodeName == "place":
                    if item.firstChild is not None:
                        place = item.firstChild.data
                    else:
                        place = "정보없음"
                elif item.nodeName == "realmName":
                    if item.firstChild is not None:
                        realmName = item.firstChild.data
                    else:
                        realmName = "정보없음"
                elif item.nodeName == "area":
                    if item.firstChild is not None:
                        area = item.firstChild.data
                    else:
                        area = "정보없음"
                elif item.nodeName == "gpsX":
                    if item.firstChild is not None:
                        gpsX = item.firstChild.data
                    else:
                        gpsX = 0
                elif item.nodeName == "gpsY":
                    if item.firstChild is not None:
                        gpsY = item.firstChild.data
                    else:
                        gpsY = 0
            DataList.append((seq, title, startDate, endDate, place, realmName, area, gpsX, gpsY))
    return DataList

def extractData_SpecificPerfor(strXml):
    global DataList
    DataList.clear()
    dom = parseString(strXml)
    strXml = dom
    PerforList = strXml.childNodes
    response = PerforList[0].childNodes
    body = response[1].childNodes
    items = body[1].childNodes
    for item in items:
        if item.nodeName == "seq":
            seq = item.firstChild.data
        elif item.nodeName == "title":
            title = item.firstChild.data
        elif item.nodeName == "startDate":
            if item.firstChild is not None:
                startDate = item.firstChild.data
            else:
                startDate = "정보없음"
        elif item.nodeName == "endDate":
            if item.firstChild is not None:
                endDate = item.firstChild.data
            else:
                endDate = "정보없음"
        elif item.nodeName == "place":
            if item.firstChild is not None:
                place = item.firstChild.data
            else:
                place = "정보없음"
        elif item.nodeName == "realmName":
            if item.firstChild is not None:
                realmName = item.firstChild.data
            else:
                realmName = "정보없음"
        elif item.nodeName == "area":
            if item.firstChild is not None:
                area = item.firstChild.data
            else:
                area = "정보없음"
        elif item.nodeName == "subTitle":
            if item.firstChild is not None:
                subTitle = item.firstChild.data
            else:
                subTitle = "정보없음"
        elif item.nodeName == "price":
            if item.firstChild is not None:
                price = item.firstChild.data
            else:
                price = "정보없음"
        elif item.nodeName == "contents1":
            if item.firstChild is not None:
                contents1 = item.firstChild.data
            else:
                contents1 = "정보없음"
        elif item.nodeName == "contents2":
            if item.firstChild is not None:
                contents2 = item.firstChild.data
            else:
                contents2 = "정보없음"
        elif item.nodeName == "url":
            if item.firstChild is not None:
                url = item.firstChild.data
            else:
                url = "정보없음"
        elif item.nodeName == "phone":
            if item.firstChild is not None:
                phone = item.firstChild.data
            else:
                phone = "정보없음"
        elif item.nodeName == "imgUrl":
            if item.firstChild is not None:
                imgUrl = item.firstChild.data
            else:
                imgUrl = "정보없음"
        elif item.nodeName == "gpsX":
            if item.firstChild is not None:
                gpsX = item.firstChild.data
            else:
                gpsX = 0
        elif item.nodeName == "gpsY":
            if item.firstChild is not None:
                gpsY = item.firstChild.data
            else:
                gpsY = 0
        elif item.nodeName == "placeAddr":
            if item.firstChild is not None:
                placeAddr = item.firstChild.data
            else:
                placeAddr = "정보없음"
    DataList.append((seq, title, startDate, endDate, place, realmName, area, subTitle, price, contents1, contents2,
                     url, phone, imgUrl, gpsX, gpsY, placeAddr))
    return DataList