import pickle
from tkinter import Tk,Button,Label,StringVar,Entry,DoubleVar
import os
def mailer():
	emailf=open('email_conf.pkl','wb+')
	li=[]
	li.append(name.get())
	li.append(mailid.get())
	pickle.dump(li,emailf)
	emailf.close()


def urlnew():
	urlf=open('link_conf.pkl','wb+')
	li=[]
	li.append(URL.get())
	li.append(price.get())
	lif=[]
	lif.append(li)
	pickle.dump(lif,urlf)
	urlf.close()
def urlapp():
	urlf=open('link_conf.pkl','rb')
	lia=pickle.load(urlf)
	urlf.close()
	urlf=open('link_conf.pkl','wb+')
	li=[]
	li.append(URL.get())
	li.append(price.get())
	lia.append(li)
	pickle.dump(lia,urlf)
	urlf.close()

def dele():
	os.remove("link_conf.pkl")


window=Tk()
window.title("Amazon Price Tracker")
window.configure(background='black')
window.geometry('720x480')
window.resizable(width=False,height=False)


Name=Label(window,text='Enter Your Name',width=14,bg='grey',fg='black')
Name.grid(column=0,row=0,padx=20,pady=20)
name=StringVar()
Namen=Entry(window,textvariable=name,width=20,fg='black',bg='grey')
Namen.grid(column=1,row=0,pady=20,padx=20)
Namen.delete(0,'end')

email=Label(window,text='Enter Your Email ID',width=14,bg='grey',fg='black')
email.grid(column=2,row=0,padx=20,pady=20)
mailid=StringVar()
emailen=Entry(window,textvariable=mailid,width=20,fg='black',bg='grey')
emailen.grid(column=3,row=0,pady=20,padx=20)
emailen.delete(0,'end')

Update=Button(window,text='Update',bg='red',fg='black',width=11,command=mailer)
Update.grid(column=4,row=0,padx=20,pady=20)

URLL=Label(window,text='Enter the URL',width=14,bg='grey',fg='black')
URLL.grid(column=0,row=1,padx=20,pady=20)
URL=StringVar()
URLen=Entry(window,textvariable=URL,width=20,fg='black',bg='grey')
URLen.grid(column=1,row=1,pady=20,padx=20)
URLen.delete(0,'end')

priceL=Label(window,text='Enter the Price',width=14,bg='grey',fg='black')
priceL.grid(column=0,row=2,padx=20,pady=20)
price=DoubleVar()
priceen=Entry(window,textvariable=price,width=20,fg='black',bg='grey')
priceen.grid(column=1,row=2,pady=20,padx=20)
priceen.delete(0,'end')

AddToNew=Button(window,text='AddToNew',bg='red',fg='black',width=14,command=urlnew)
AddToNew.grid(column=0,row=4,padx=20,pady=20)

Appendex=Button(window,text='AppendExisting',bg='red',fg='black',width=14,command=urlapp)
Appendex.grid(column=1,row=4,padx=20,pady=20)

Deletef=Button(window,text='Delete Existing',bg='red',fg='black',width=14,command=dele)
Deletef.grid(column=2,row=4,padx=20,pady=20)

window.mainloop()