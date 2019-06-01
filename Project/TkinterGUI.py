from tkinter import *
from tkinter import ttk
from tkinter import font
from io import BytesIO
import urllib
import urllib.request
from PIL import Image, ImageTk

import tkinter.messagebox
import random
from openapi_uri import *
from gmail import *

root = Tk()

root.geometry("500x500+500+200")
root.withdraw()
#label = Label(root)
#label = Label(top)
im = None
#image = None

g_Tk = Tk()
#g_Tk.geometry("800x600+750+200")
g_Tk.geometry("1000x610+200+50")


Maplabel = Label(g_Tk, bg='gray', width=33, height=16)
Maplabel.place(x=740, y=340)

g_Tk.title("공연 / 전시 정보 조회 서비스")
SearchMode = 3
TempFont1 = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
TempFont2 = font.Font(g_Tk, size=10, weight='bold', family='Consolas')
SearchLabel = Label(g_Tk, font=TempFont1, text="지역별 검색")
OptionLabel1 = Label(g_Tk, font=TempFont2, text="시/도")
OptionLabel2 = Label(g_Tk, font=TempFont2, text="구/군")
InputLabel1 = Entry(g_Tk, width=18, borderwidth=6, relief='ridge')
InputLabel2 = Entry(g_Tk, width=18, borderwidth=6, relief='ridge')
InputLabel3 = Entry(g_Tk, width=18, borderwidth=6, relief='ridge')
RealmComboBox = ttk.Combobox(g_Tk, width=15, value=["연극", "음악", "무용", "미술", "건축", "영상", "문학", "문화정책",
                                                    "축제문화공간", "기타"])


# 타이틀 표시
def InitTopText():
    TempFont = font.Font(g_Tk, size=20, weight='bold', family='Consolas')
    MainText = Label(g_Tk, font=TempFont, text="[공연/전시 정보검색 서비스]")
    MainText.place(x=300, y=10)
    SpecificSearchLabel = Label(g_Tk, font=TempFont2, text="일련번호")
    SpecificSearchLabel.place(x=360, y=70)
    InputLabel3.place(x=430, y=65)

# 기능별 버튼 출력
def SearchCategoryButton():
    AreaSearch = Button(g_Tk, font=TempFont1, text="지역별", command=InitSearchByArea)
    AreaSearch.place(x=10, y=10)
    PeriodSearch = Button(g_Tk, font=TempFont1, text="기간별", command=InitSearchByPeriod)
    PeriodSearch.place(x=100, y=10)
    RealmSearch = Button(g_Tk, font=TempFont1, text="분야별", command=InitSearchByRealm)
    RealmSearch.place(x=190, y=10)

# 지역별 버튼 클릭
def InitSearchByArea():
    global SearchMode
    SearchMode = 0
    RealmComboBox.place_forget()
    SearchLabel.config(text="지역별 검색")
    SearchLabel.place(x=130, y=60)
    OptionLabel1.config(text="시/도")
    OptionLabel1.place(x=30, y=100)
    OptionLabel2.config(text="구/군")
    OptionLabel2.place(x=30, y=150)
    InputLabel1.place(x=80, y=95)
    InputLabel1.delete(0, END)
    InputLabel2.place(x=80, y=145)
    InputLabel2.delete(0, END)

# 기간별 버튼 클릭
def InitSearchByPeriod():
    global SearchMode
    SearchMode = 1
    RealmComboBox.place_forget()
    SearchLabel.config(text="기간별 검색")
    SearchLabel.place(x=130, y=60)
    OptionLabel1.config(text="시작 연월일")
    OptionLabel1.place(x=30, y=100)
    OptionLabel2.config(text="종료 연월일")
    OptionLabel2.place(x=30, y=150)
    InputLabel1.place(x=110, y=95)
    InputLabel1.delete(0, END)
    InputLabel2.place(x=110, y=145)
    InputLabel2.delete(0, END)

# 분야별 버튼 클릭
def InitSearchByRealm():
    global SearchMode
    SearchMode = 2
    OptionLabel2.place_forget()
    InputLabel1.place_forget()
    InputLabel2.place_forget()
    SearchLabel.config(text="분야별 검색")
    SearchLabel.place(x=130, y=60)
    OptionLabel1.config(text="분야")
    OptionLabel1.place(x=30, y=100)
    RealmComboBox.place(x=80, y=100)

# 검색 버튼 출력
def InitSearchButton():
    SearchButton = Button(g_Tk, font=TempFont2, text="검색",  command=SearchButtonAction)
    SearchButton.place(x=270, y=125)
    SpecificSearchButton = Button(g_Tk, font=TempFont2, text="검색", command=SpecificSearchButtonAction)
    SpecificSearchButton.place(x=600, y=65)
    SendingEmailButton = Button(g_Tk, font=TempFont2, text="E-mail", command=SendingMailButtonAction)
    SendingEmailButton.place(x=660, y=65)

# 이메일 버튼 클릭
def SendingMailButtonAction():
    SendingMail(DataList)

# 검색 버튼 클릭
def SearchButtonAction():
    global SearchListBox, SearchMode
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    if SearchMode == 0: #지역별 검색
        DisplayPerforList(getApi_SearchByArea(InputLabel1.get(), InputLabel2.get(), 999))
    elif SearchMode == 1: #기간별 검색
        DisplayPerforList(getApi_SearchByPeriod(InputLabel1.get(), InputLabel2.get(), 999))
    elif SearchMode == 2: #분야별 검색
        DisplayPerforList(getApi_SearchByRealm(RealmComboBox.get(), 999))
    RenderText.configure(state='disabled')

# 상세 검색 버튼 클릭
def SpecificSearchButtonAction():
    global SearchListBox, SearchMode
    RenderText2.configure(state='normal')
    RenderText2.delete(0.0, END)
    DisplaySpecificInfo(getApi_SearchBySeq(InputLabel3.get()))
    RenderText.configure(state='disabled')

# 공연전시 리스트 출력
def DisplayPerforList(DataList):
    for i in range(len(DataList)):
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "] ")
        RenderText.insert(INSERT, "일련번호: ")
        RenderText.insert(INSERT, DataList[i][0])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "제목: ")
        RenderText.insert(INSERT, DataList[i][1])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "시작일: ")
        RenderText.insert(INSERT, DataList[i][2])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "마감일: ")
        RenderText.insert(INSERT, DataList[i][3])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "장소: ")
        RenderText.insert(INSERT, DataList[i][4])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "분류: ")
        RenderText.insert(INSERT, DataList[i][5])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "지역: ")
        RenderText.insert(INSERT, DataList[i][6])
        RenderText.insert(INSERT, "\n\n")

# 공연전시 세부정보 출력
def DisplaySpecificInfo(DataList):
    #for i in range(len(DataList)):
    RenderText2.insert(INSERT, "[일련번호]")
    RenderText2.insert(INSERT, "\n")
    RenderText2.insert(INSERT, DataList[0][0])
    RenderText2.insert(INSERT, "\n\n")
    RenderText2.insert(INSERT, "[제목]")
    RenderText2.insert(INSERT, "\n")
    RenderText2.insert(INSERT, DataList[0][1])
    RenderText2.insert(INSERT, "\n\n")
    RenderText2.insert(INSERT, "[시작일]")
    RenderText2.insert(INSERT, "\n")
    RenderText2.insert(INSERT, DataList[0][2])
    RenderText2.insert(INSERT, "\n\n")
    RenderText2.insert(INSERT, "[마감일]")
    RenderText2.insert(INSERT, "\n")
    RenderText2.insert(INSERT, DataList[0][3])
    RenderText2.insert(INSERT, "\n\n")
    RenderText2.insert(INSERT, "[장소]")
    RenderText2.insert(INSERT, "\n")
    RenderText2.insert(INSERT, DataList[0][4])
    RenderText2.insert(INSERT, "\n\n")
    RenderText2.insert(INSERT, "[분류]")
    RenderText2.insert(INSERT, "\n")
    RenderText2.insert(INSERT, DataList[0][5])
    RenderText2.insert(INSERT, "\n\n")
    RenderText2.insert(INSERT, "[지역]")
    RenderText2.insert(INSERT, "\n")
    RenderText2.insert(INSERT, DataList[0][6])
    RenderText2.insert(INSERT, "\n\n")
    RenderText2.insert(INSERT, "[부제]")
    RenderText2.insert(INSERT, "\n")
    RenderText2.insert(INSERT, DataList[0][7])
    RenderText2.insert(INSERT, "\n\n")
    RenderText2.insert(INSERT, "[가격]")
    RenderText2.insert(INSERT, "\n")
    RenderText2.insert(INSERT, DataList[0][8])
    RenderText2.insert(INSERT, "\n\n")
    RenderText2.insert(INSERT, "[주내용]")
    RenderText2.insert(INSERT, "\n")
    RenderText2.insert(INSERT, DataList[0][9])
    RenderText2.insert(INSERT, "\n\n")
    RenderText2.insert(INSERT, "[소내용]")
    RenderText2.insert(INSERT, "\n")
    RenderText2.insert(INSERT, DataList[0][10])
    RenderText2.insert(INSERT, "\n\n")
    RenderText2.insert(INSERT, "[URL 주소]")
    RenderText2.insert(INSERT, "\n")
    RenderText2.insert(INSERT, DataList[0][11])
    RenderText2.insert(INSERT, "\n\n")
    RenderText2.insert(INSERT, "[연락처]")
    RenderText2.insert(INSERT, "\n")
    RenderText2.insert(INSERT, DataList[0][12])
    RenderText2.insert(INSERT, "\n\n")

    DisplayImage(DataList[0][13])
    #RenderText2.window_create(INSERT, create=DisplayImage(DataList[0][13]))
    #label.config(image=DisplayImage(DataList[0][13]))
    #RenderText2.window_create(INSERT, window=label)
    #RenderText2.image_create(INSERT, image=DisplayImage(DataList[0][13]))

    RenderText2.insert(INSERT, "[상세 주소]")
    RenderText2.insert(INSERT, "\n")
    RenderText2.insert(INSERT, DataList[0][16])
    RenderText2.insert(INSERT, "\n\n")

# 안씀
def SearchLibrary():
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("openAPI.seoul.go.kr:8088")
    conn.request("GET", "/6b4f54647867696c3932474d68794c/xml/GeoInfoLibrary/1/800")
    req = conn.getresponse()
    #global DataList
    #DataList.clear()

    if req.status == 200:
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
            parseData = parseString(BooksDoc)
            GeoInfoLibrary = parseData.childNodes
            row = GeoInfoLibrary[0].childNodes
            for item in row:
                if item.nodeName == "row":
                    subitems = item.childNodes
                    if subitems[3].firstChild.nodeValue == InputLabel.get():  #
                        pass
                    elif subitems[5].firstChild.nodeValue == InputLabel.get():  #
                        pass
                    else:
                        continue
                    if subitems[29].firstChild is not None:
                        tel = str(subitems[29].firstChild.nodeValue)
                        pass  #
                        if tel[0] is not '0':
                            tel = "02-" + tel
                            pass
                        DataList.append((subitems[15].firstChild.nodeValue, subitems[13].firstChild.nodeValue, tel))
                    else:
                        DataList.append((subitems[15].firstChild.nodeValue, subitems[13].firstChild.nodeValue, "-"))
            for i in range(len(DataList)):
                RenderText.insert(INSERT, "[")
                RenderText.insert(INSERT, i + 1)
                RenderText.insert(INSERT, "] ")
                RenderText.insert(INSERT, "시설명: ")
                RenderText.insert(INSERT, DataList[i][0])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "주소: ")
                RenderText.insert(INSERT, DataList[i][1])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "전화번호: ")
                RenderText.insert(INSERT, DataList[i][2])
                RenderText.insert(INSERT, "\n\n")

# 공연전시 리스트 창
def InitRenderText():
    global RenderText
    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderText = Text(g_Tk, width=40, height=29, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10, y=190)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.place(x=320, y=190)
    RenderText.configure(state='disabled')

# 공연전시 세부정보 창
def InitSpecificRenderText():
    global RenderText2
    RenderTextScrollbar2 = Scrollbar(g_Tk)
    RenderText2 = Text(g_Tk, width=49, height=36, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar2.set)
    RenderText2.pack()
    RenderText2.place(x=350, y=100)
    RenderTextScrollbar2.config(command=RenderText2.yview)
    RenderTextScrollbar2.place(x=720, y=100)
    RenderText.configure(state='disabled')

# 공연전시 이미지 출력
def DisplayImage(url):
    global im
    top = Toplevel()
    #root.geometry("500x500+500+200")
    #root.deiconify()

    #url = "http://tong.visitkorea.or.kr/cms/resource/74/2396274_image2_1.JPG"
    with urllib.request.urlopen(url) as u:
        raw_data = u.read()
    im = Image.open(BytesIO(raw_data))
    image = ImageTk.PhotoImage(im)
    #label = Label(g_Tk, image=image)
    Imagelabel = Label(top, bg='gray', width=33, height=16)
    Imagelabel.place(x=740, y=70)
    Imagelabel.config(image=image)
    #Imagelabel.pack()
    #root.mainloop()

    #return image
    #imagelabel.config(image=image, height=400, width=400)
    #imagelabel.pack()
    #imagelabel.place(x=0, y=0)
    #root.mainloop()


    #im = Image.open(BytesIO(raw_data))
    #image = ImageTk.PhotoImage(master=RenderText2,image=im)
    #label = Label(RenderText2, image=image, height=300, width=300)



SearchButton = Button(g_Tk, text="검색",  command=SearchButtonAction)

SearchCategoryButton()
InitTopText()
InitSearchByArea()
InitSearchButton()

InitRenderText()
InitSpecificRenderText()
#InitSendEmailButton()
#InitSortListBox()
#InitSortButton()


g_Tk.mainloop()