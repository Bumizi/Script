#!/usr/bin/python
# coding=utf-8

import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback

from openapi_uri import *

#key = 'sea100UMmw23Xycs33F1EQnumONR%2F9ElxBLzkilU9Yr1oT4TrCot8Y2p0jyuJP72x9rG9D8CN5yuEs6AS2sAiw%3D%3D'
key = '5jJOAyIYEGAq71RHF1AMCi8%2F0s%2Fw0G9%2FWlxzhjXUpSNItx2%2FeaCs9kruHWarDxWgAZOTCXtbeuVXbupzdqDm%2FQ%3D%3D'
TOKEN = '847129529:AAGiMAMXwttGPhDGD3tw8oJwZJMS4I7xWXo'
MAX_MSG_LENGTH = 300
#baseurl = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?ServiceKey='+key

baseurl = 'http://www.culture.go.kr/openapi/rest/publicperformancedisplays/area'+'?'+key

bot = telepot.Bot(TOKEN)

def getAreaData(sido, gugun):
    res_list = []
    url = baseurl+'&sido='+sido+'&gugun='+gugun+'&rows=999'
    #print(url)
    res_body = urlopen(url).read()
    #print(res_body)
    soup = BeautifulSoup(res_body, 'html.parser')
    items = soup.findAll('item')
    for item in items:
        print(item)
        item = re.sub('<.*?>', '|', item.text)
        print(item)
        parsed = item.split('|')
        print(parsed)
        try:
            row = parsed[3]+'/'+parsed[6]+'/'+parsed[7]+', '+parsed[4]+' '+parsed[5]+', '+parsed[8]+', '+parsed[11]+', '+parsed[1].strip()+'\n'
        except IndexError:
            row = item.replace('|', ',')

        if row:
            res_list.append(row.strip())
    return res_list

def getPeriodData(start, end):
    res_list = []
    url = baseurl+'&from='+start+'&to='+end+'&rows=999'
    #print(url)
    res_body = urlopen(url).read()
    #print(res_body)
    soup = BeautifulSoup(res_body, 'html.parser')
    items = soup.findAll('item')
    for item in items:
        print(item)
        item = re.sub('<.*?>', '|', item.text)
        print(item)
        parsed = item.split('|')
        print(parsed)
        try:
            row = parsed[3]+'/'+parsed[6]+'/'+parsed[7]+', '+parsed[4]+' '+parsed[5]+', '+parsed[8]+', '+parsed[11]+', '+parsed[1].strip()+'\n'
        except IndexError:
            row = item.replace('|', ',')

        if row:
            res_list.append(row.strip())
    return res_list

def getRealmData(realm):
    res_list = []
    url = baseurl+'&realmCode='+realm+'&rows=999'
    #print(url)
    res_body = urlopen(url).read()
    #print(res_body)
    soup = BeautifulSoup(res_body, 'html.parser')
    items = soup.findAll('item')
    for item in items:
        print(item)
        item = re.sub('<.*?>', '|', item.text)
        print(item)
        parsed = item.split('|')
        print(parsed)
        try:
            row = parsed[3]+'/'+parsed[6]+'/'+parsed[7]+', '+parsed[4]+' '+parsed[5]+', '+parsed[8]+', '+parsed[11]+', '+parsed[1].strip()+'\n'
        except IndexError:
            row = item.replace('|', ',')

        if row:
            res_list.append(row.strip())
    return res_list



def getTestData(start, end):
    res_list = []
    url = baseurl+'&from='+start+'&to='+end+'&rows=999'
    #print(url)
    res_body = urlopen(url).read()
    #print(res_body)
    soup = BeautifulSoup(res_body, 'html.parser')
    items = soup.findAll('item')
    for item in items:
        print(item)
        item = re.sub('<.*?>', '|', item.text)
        print(item)
        parsed = item.split('|')
        print(parsed)
        try:
            row = parsed[3]+'/'+parsed[6]+'/'+parsed[7]+', '+parsed[4]+' '+parsed[5]+', '+parsed[8]+', '+parsed[11]+', '+parsed[1].strip()+'\n'
        except IndexError:
            row = item.replace('|', ',')

        if row:
            res_list.append(row.strip())
    return res_list










def sendMessage(user, msg):
    try:
        bot.sendMessage(user, msg)
    except:
        traceback.print_exc(file=sys.stdout)

def run(date_param, param='11710'):
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS logs( user TEXT, log TEXT, PRIMARY KEY(user, log) )')
    conn.commit()

    user_cursor = sqlite3.connect('users.db').cursor()
    user_cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    user_cursor.execute('SELECT * from users')

    for data in user_cursor.fetchall():
        user, param = data[0], data[1]
        print(user, date_param, param)
        #res_list = getPeriodData(param, date_param)
        res_list = getApi_SearchByPeriod(param, date_param, 999)
        msg = ''
        for r in res_list:
            try:
                cursor.execute('INSERT INTO logs (user,log) VALUES ("%s", "%s")' % (user, r))
            except sqlite3.IntegrityError:
                # 이미 해당 데이터가 있다는 것을 의미합니다.
                pass
            else:
                print(str(datetime.now()).split('.')[0], r)
                if len(r+msg)+1 > MAX_MSG_LENGTH:
                    sendMessage(user, msg)
                    msg = r+'\n'
                else:
                    msg += r+'\n'
        if msg:
            sendMessage(user, msg)
    conn.commit()

if __name__ == '__main__':
    today = date.today()
    current_month = today.strftime('%Y%m')

    print('[', today, ']received token :', TOKEN)

    pprint(bot.getMe())

    run(current_month)
