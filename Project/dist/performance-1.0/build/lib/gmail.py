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

    for perforitem in List:
        # create bold element
        #b = newdoc.createElement('b')
        # create text node
        #ibsnText = newdoc.createTextNode("ISBN:" + perforitem[0])
        #b.appendChild(ibsnText)

        #body.appendChild(b)

        # BR 태그 (엘리먼트) 생성.
        br = newdoc.createElement('br')
        body.appendChild(br)

        # create title Element
        seq = newdoc.createElement('p')
        # create text node
        seqText = newdoc.createTextNode("Seq : " + perforitem[0])
        title = newdoc.createElement('p')
        titleText = newdoc.createTextNode("Title : " + perforitem[1])
        startDate = newdoc.createElement('p')
        startDateText = newdoc.createTextNode("Start Date : " + perforitem[2])
        endDate = newdoc.createElement('p')
        endDateText = newdoc.createTextNode("End Date : " + perforitem[3])
        place = newdoc.createElement('p')
        placeText = newdoc.createTextNode("Place : " + perforitem[4])
        realmName = newdoc.createElement('p')
        realmNameText = newdoc.createTextNode("Realm Name : " + perforitem[5])
        area = newdoc.createElement('p')
        areaText = newdoc.createTextNode("Area : " + perforitem[6])
        subTitle = newdoc.createElement('p')
        subTitleText = newdoc.createTextNode("SubTitle : " + perforitem[7])
        price = newdoc.createElement('p')
        priceText = newdoc.createTextNode("Price : " + perforitem[8])
        contents1 = newdoc.createElement('p')
        contents1Text = newdoc.createTextNode("Contents1 : " + perforitem[9])
        contents2 = newdoc.createElement('p')
        contents2Text = newdoc.createTextNode("Contents2 : " + perforitem[10])
        url = newdoc.createElement('p')
        urlText = newdoc.createTextNode("URL : " + perforitem[11])
        phone = newdoc.createElement('p')
        phoneText = newdoc.createTextNode("Phone : " + perforitem[12])
        placeAddr = newdoc.createElement('p')
        placeAddrText = newdoc.createTextNode("Place Addr : " + perforitem[16])

        seq.appendChild(seqText)
        title.appendChild(titleText)
        startDate.appendChild(startDateText)
        endDate.appendChild(endDateText)
        place.appendChild(placeText)
        realmName.appendChild(realmNameText)
        area.appendChild(areaText)
        subTitle.appendChild(subTitleText)
        price.appendChild(priceText)
        contents1.appendChild(contents1Text)
        contents2.appendChild(contents2Text)
        url.appendChild(urlText)
        phone.appendChild(phoneText)
        placeAddr.appendChild(placeAddrText)

        body.appendChild(seq)
        body.appendChild(br)  # line end
        body.appendChild(title)
        body.appendChild(br)  # line end
        body.appendChild(startDate)
        body.appendChild(br)  # line end
        body.appendChild(endDate)
        body.appendChild(br)  # line end
        body.appendChild(place)
        body.appendChild(br)  # line end
        body.appendChild(realmName)
        body.appendChild(br)  # line end
        body.appendChild(area)
        body.appendChild(br)  # line end
        body.appendChild(subTitle)
        body.appendChild(br)  # line end
        body.appendChild(price)
        body.appendChild(br)  # line end
        body.appendChild(contents1)
        body.appendChild(br)  # line end
        body.appendChild(contents2)
        body.appendChild(br)  # line end
        body.appendChild(url)
        body.appendChild(br)  # line end
        body.appendChild(phone)
        body.appendChild(br)  # line end
        body.appendChild(placeAddr)
        body.appendChild(br)  # line end

    # append Body
    top_element.appendChild(body)

    return newdoc.toxml()


def SendingMail(content):
    host = "smtp.gmail.com" # Gmail STMP 서버 주소.
    port = "587"

    senderAddr = "bumizi95@gmail.com"     # 보내는 사람 email 주소.
    recipientAddr = "bumizi95@naver.com"   # 받는 사람 email 주소.

    msgtext = "testing now"
    passwd = "rlfrkaptnl"

    html = MakeHtmlDoc(DataList)

    msg = MIMEBase("multipart", "alternative")
    msg['Subject'] = "공연/전시 세부 정보"
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    msgPart = MIMEText(msgtext, 'plain')
    perforPart = MIMEText(html, 'html', _charset='UTF-8')

    # 만들었던 mime을 MIMEBase에 첨부 시킨다.
    # 메세지에 생성한 MIME 문서를 첨부합니다.
    msg.attach(msgPart)
    msg.attach(perforPart)

    # 메일을 발송한다.
    s = mysmtplib.MySMTP(host, port)
    #s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)
    s.sendmail(senderAddr , [recipientAddr], msg.as_string())
    s.close()
