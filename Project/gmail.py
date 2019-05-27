# -*- coding: utf-8 -*-
import mimetypes
import mysmtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from openapi_uri import *

def MakeHtmlDoc(List):
    from xml.dom.minidom import getDOMImplementation
    # get Dom Implementation
    impl = getDOMImplementation()

    newdoc = impl.createDocument(None, "html", None)  # DOM 객체 생성
    top_element = newdoc.documentElement
    header = newdoc.createElement('header')
    top_element.appendChild(header)

    # Body 엘리먼트 생성.
    body = newdoc.createElement('body')

    for bookitem in List:
        # create bold element
        b = newdoc.createElement('b')
        # create text node
        ibsnText = newdoc.createTextNode("ISBN:" + bookitem[0])
        b.appendChild(ibsnText)

        body.appendChild(b)

        # BR 태그 (엘리먼트) 생성.
        br = newdoc.createElement('br')

        body.appendChild(br)

        # create title Element
        p = newdoc.createElement('p')
        # create text node
        titleText = newdoc.createTextNode("Title:" + bookitem[1])
        p.appendChild(titleText)

        body.appendChild(p)
        body.appendChild(br)  # line end

    # append Body
    top_element.appendChild(body)

    return newdoc.toxml()


def SendingMail(content):
    host = "smtp.gmail.com" # Gmail STMP 서버 주소.
    port = "587"

    senderAddr = "bumizi95@gmail.com"     # 보내는 사람 email 주소.
    recipientAddr = "bumizi95@naver.com"   # 받는 사람 email 주소.

    title = 'test'

    msgtext = "testing now"
    passwd = "rlfrkaptnl"

    html = MakeHtmlDoc(DataList)

    msg = MIMEBase("multipart", "alternative")
    msg['Subject'] = title
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    # Message container를 생성합니다.
    msg = MIMEMultipart('alternative')

    msgPart = MIMEText(msgtext, 'plain')
    bookPart = MIMEText(html, 'html', _charset='UTF-8')

    html = MakeHtmlDoc(content)

    # 만들었던 mime을 MIMEBase에 첨부 시킨다.
    # 메세지에 생성한 MIME 문서를 첨부합니다.
    msg.attach(msgPart)
    msg.attach(bookPart)

    # 메일을 발송한다.
    s = mysmtplib.MySMTP(host, port)
    #s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)
    s.sendmail(senderAddr , [recipientAddr], msg.as_string())
    s.close()
