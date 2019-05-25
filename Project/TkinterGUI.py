from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import random
#import openapi_uri

g_Tk = Tk()
g_Tk.geometry("800x600+750+200")
g_Tk.title("공연 / 전시 정보 조회 서비스")
DataList = []
SearchMode = 3
SearchLabel = Label(g_Tk, text="지역별 검색")
SpecificSearchLabel = Label(g_Tk, text="일련번호")
OptionLabel1 = Label(g_Tk, text="시/도")
OptionLabel2 = Label(g_Tk, text="구/군")
InputLabel1 = Entry(g_Tk, width=18, borderwidth=6, relief='ridge')
InputLabel2 = Entry(g_Tk, width=18, borderwidth=6, relief='ridge')

RealmComboBox = ttk.Combobox(g_Tk, width=15, value=["연극", "음악", "무용", "미술", "건축", "영상", "문학", "문화정책",
                                                    "축제문화공간", "기타"])

# 타이틀 표시
def InitTopText():
    MainText = Label(g_Tk, text="[공연 / 전시 정보검색 서비스]")
    MainText.place(x=330)
    SpecificSearchLabel = Label(g_Tk, text="일련번호")
    SpecificSearchLabel.place(x=420, y=70)
    InputLabel3 = Entry(g_Tk, width=18, borderwidth=6, relief='ridge')
    InputLabel3.place(x=480, y=65)

# 기능별 버튼 생성
def SearchCategoryButton():
    AreaSearch = Button(g_Tk, text="지역별", command=InitSearchByArea)
    AreaSearch.place(x=10, y=10)
    PeriodSearch = Button(g_Tk, text="기간별", command=InitSearchByPeriod)
    PeriodSearch.place(x=70, y=10)
    RealmSearch = Button(g_Tk, text="분야별", command=InitSearchByRealm)
    RealmSearch.place(x=130, y=10)

# 지역별 버튼 클릭 시 UI
def InitSearchByArea():
    global SearchMode
    SearchMode = 0
    RealmComboBox.place_forget()
    SearchButton.place(x=320, y=125)
    SearchLabel.config(text="지역별 검색")
    SearchLabel.place(x=130, y=50)
    OptionLabel1.config(text="시/도")
    OptionLabel1.place(x=30, y=100)
    OptionLabel2.config(text="구/군")
    OptionLabel2.place(x=30, y=150)
    InputLabel1.place(x=80, y=95)
    InputLabel2.place(x=80, y=145)

# 기간별 버튼 클릭 시 UI
def InitSearchByPeriod():
    global SearchMode
    SearchMode = 1
    RealmComboBox.place_forget()
    SearchButton.place(x=320, y=125)
    SearchLabel.config(text="기간별 검색")
    SearchLabel.place(x=130, y=50)
    OptionLabel1.config(text="시작 연월일")
    OptionLabel1.place(x=30, y=100)
    OptionLabel2.config(text="종료 연월일")
    OptionLabel2.place(x=30, y=150)
    InputLabel1.place(x=110, y=95)
    InputLabel2.place(x=110, y=145)

# 분야별 버튼 클릭 시 UI
def InitSearchByRealm():
    global SearchMode
    SearchMode = 2
    SearchButton.place(x=320, y=125)
    OptionLabel2.place_forget()
    InputLabel1.place_forget()
    InputLabel2.place_forget()
    SearchLabel.config(text="분야별 검색")
    SearchLabel.place(x=130, y=50)
    OptionLabel1.config(text="분야")
    OptionLabel1.place(x=30, y=100)
    RealmComboBox.place(x=80, y=100)

def InitSearchListBox():
    global SearchListBox
    ListBoxScrollbar = Scrollbar(g_Tk)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=1500, y=50)
    SearchListBox = Listbox(g_Tk, activestyle='none', width=10, height=1, borderwidth=12, relief='ridge', yscrollcommand=ListBoxScrollbar.set)
    SearchListBox.insert(1, "도서관")
    SearchListBox.insert(2, "모범음식점")
    SearchListBox.insert(3, "마트")
    SearchListBox.insert(4, "문화시설")
    SearchListBox.pack()
    SearchListBox.place(x=500, y=50)
    ListBoxScrollbar.config(command=SearchListBox.yview)

#일단 안씀
def InitInputLabel():
    global InputLabel
    InputLabel = Entry(g_Tk, width = 26, borderwidth = 12, relief = 'ridge')
    InputLabel.pack()
    InputLabel.place(x=500, y=105)

#일단 안씀
def InitSearchButton():
    SearchButton = Button(g_Tk, text="검색",  command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=320, y=125)
    pass

def InitSearchButton2():
    SearchButton = Button(g_Tk, text="검색",  command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=650, y=65)

def SearchButtonAction():
    global SearchListBox, SearchMode
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)

    if SearchMode == 0: #지역별 검색
        pass
    elif SearchMode == 1: #기간별 검색
        pass
    elif SearchMode == 2: #분야별 검색
        pass

    iSearchIndex = SearchListBox.curselection()[0]
    if iSearchIndex == 0:
        SearchLibrary()
    elif iSearchIndex == 1:
        pass#SearchGoodFoodService()
    elif iSearchIndex == 2:
        pass#SearchMarket()
    elif iSearchIndex == 3:
        pass#SearchCultural()
    RenderText.configure(state='disabled')

def SearchLibrary():
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("openAPI.seoul.go.kr:8088")
    conn.request("GET", "/6b4f54647867696c3932474d68794c/xml/GeoInfoLibrary/1/800")
    req = conn.getresponse()
    global DataList
    DataList.clear()
    #DataList = extractData_SearchByArea()

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


def InitRenderText():
    global RenderText
    RenderTextScrollbar = Scrollbar(g_Tk)
    #RenderTextScrollbar.pack()
    #RenderTextScrollbar.place(x=375, y=200)
    RenderText = Text(g_Tk, width=49, height=27, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10, y=215)
    RenderTextScrollbar.config(command=RenderText.yview)
    #RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)
    RenderTextScrollbar.place(x=380, y=215)
    RenderText.configure(state='disabled')

def InitRenderText2():
    global RenderText2
    RenderTextScrollbar2 = Scrollbar(g_Tk)
    #RenderTextScrollbar2.pack()
    #RenderTextScrollbar2.place(x=375, y=100)
    RenderText2 = Text(g_Tk, width=49, height=36, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar2.set)
    RenderText2.pack()
    RenderText2.place(x=410, y=100)
    RenderTextScrollbar2.config(command=RenderText.yview)
    #RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)
    RenderTextScrollbar2.place(x=780, y=100)
    RenderText.configure(state='disabled')


SearchButton = Button(g_Tk, text="검색",  command=SearchButtonAction)

SearchCategoryButton()
InitTopText()
#InitSearchListBox()

InitInputLabel()
#InitSearchButton()
InitSearchButton2()

InitRenderText()
InitRenderText2()
#InitSendEmailButton()
#InitSortListBox()
#InitSortButton()
g_Tk.mainloop()

