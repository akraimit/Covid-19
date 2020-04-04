from plyer import notification
import requests
import time
from bs4 import BeautifulSoup

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = r"C:\Users\acer\Desktop\covid\covid_19_Jny_3.ico",
        timeout = 6
        )
def getdata(url):
    r = requests.get(url)
    return r.text

if __name__=="__main__":
    #notifyMe("Ashok", "Lets stop the spread of chinese virus")
    while True:
        myHtmlData = getdata('https://www.mohfw.gov.in/')
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        #print(soup.prettify())
        myDataStr = ""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            #print(tr)
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]
        itemList = myDataStr.split('\n\n')
        print(itemList)
        states = ['Chandigarh', 'Tamil Nadu', 'Uttar Pradesh']
        for item in itemList[0:29]:
            dataList= item.split('\n')
            if dataList[1] in states:
                print(dataList)
                nTitle = 'Cases of Covid-19'
                nText = f"State : {dataList[1]}\nTotal Cases : {dataList[2]}\nRecoverd : {dataList[3]}\nCorona_Marters : {dataList[4]}"
                notifyMe(nTitle, nText)
                time.sleep(2)
        time.sleep(3600)
                
