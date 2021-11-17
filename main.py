def Scrap():
    def notifyme(title,message):
        plyer.notification.notify(
            title=title,
            message=message,
            app_icon="virus.ico",
            timeout=20
        )
    url="https://www.worldometers.info/coronavirus/"
    r=requests.get(url)
    soup=BeautifulSoup(r.content,"html.parser")
    tablebody=soup.find("tbody")
    ttt=tablebody.find_all("tr")
    notifycountry=countrydata.get()
    if(notifycountry==""):
        notifycountry="india"
    countries,total_cases,new_cases,total_deaths,new_deaths,total_recovered,active_cases=[],[],[],[],[],[],[]
    serious,totalcases_permillion,totaldeaths_permillion,totaltests,totaltests_permillion=[],[],[],[],[]
    headers=["countries","total_cases","new_cases","total_deaths","new_deaths","total_recovered","active_cases",
             "serious","totalcases_permillion","totaldeaths_permillion","totaltests","totaltests_permillion"]
    for i in ttt:
        id=i.find_all("td")
        if(id[1].text.strip().lower()==notifycountry):
            totalcases1=int(id[2].text.strip().replace(",",""))
            totaldeaths1=id[4].text.strip()
            newcases1=id[6].text.strip()
            newdeaths1=id[8].text.strip()
            notifyme("Corona Virus Details In {}".format(notifycountry),
                   "Total Cases:{}\nTotal Deaths:{}\nNew Cases:{}\nNew Deaths:{}".format(totalcases1,totaldeaths1,newcases1,newdeaths1))
        countries.append(id[1].text.strip()),total_cases.append(int(id[2].text.strip().replace(",","")))
        new_cases.append(id[3].text.strip()), total_deaths.append(id[4].text.strip())
        new_deaths.append(id[5].text.strip()), total_recovered.append(id[6].text.strip())
        active_cases.append(id[7].text.strip()), serious.append(id[8].text.strip())
        totalcases_permillion.append(id[9].text.strip()), totaldeaths_permillion.append(id[10].text.strip())
        totaltests_permillion.append(id[11].text.strip()), totaltests_permillion.append(id[12].text.strip())
import plyer
import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox,filedialog
root = Tk()
root.title("Corona Virus Info ")
root.geometry("530x300+200+80")
root.configure(bg="yellow")
root.iconbitmap("virus.ico")
path=" "
formatlist=[]
IntroLabel=Label(root,text="Covid-19 Info",font=("new roman",30,"italic bold"),bg="plum2",width=22)
IntroLabel.place(x=0,y=0)
EntryLabel=Label(root,text="Enter Country : ",font=("new roman",20,"italic bold"),bg="yellow")
EntryLabel.place(x=10,y=70)
FormatLabel=Label(root,text="Download In : ",font=("new roman",20,"italic bold"),bg="yellow")
FormatLabel.place(x=10,y=150)
countrydata=StringVar()
ent1=Entry(root,textvariable=countrydata,font=("arial",20,"italic bold"),relief=RIDGE,bd=2,width=20)
ent1.place(x=220,y=70)
InHtml=Button(root,text="Html",bg="green",font=("arial",15,"italic bold"),relief=RIDGE,activebackground="white",bd=2,width=5)
InHtml.place(x=219,y=150)
InJson=Button(root,text="Json",bg="green",font=("arial",15,"italic bold"),relief=RIDGE,activebackground="white",bd=2,width=5)
InJson.place(x=338,y=150)
InCsv=Button(root,text="Csv",bg="green",font=("arial",15,"italic bold"),relief=RIDGE,activebackground="white",bd=2,width=5)
InCsv.place(x=455,y=150)
Submit=Button(root,text="Submit",bg="green",font=("arial",15,"italic bold"),relief=RIDGE,activebackground="white",bd=2,width=25,command=Scrap)
Submit.place(x=110,y=250)
root.mainloop()
