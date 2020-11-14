import requests
import time
from bs4 import BeautifulSoup
import smtplib
import pickle
headers={"User-Agent":'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'}
def check(URL,p):
	page=requests.get(URL,headers=headers)
	soup=BeautifulSoup(page.content,'html.parser')
	price=soup.find(id='priceblock_dealprice')
	price=((price.get_text()).strip())
	title=soup.find(id='productTitle').get_text()
	title=title.strip()
	temp=list(price)
	temp.remove(',')
	price=''.join(temp)
	price=float(price[2:])
	if price<p:
		mail(title,price)

def mail(title,price):
	email=open('email_conf.pkl','rb')
	temp=pickle.load(email)
	s=smtplib.SMTP('smtp.gmail.com',587)
	s.starttls()
	s.login('enteryouremail@smtp.com','password')
	body=f"{title} is now {price}"
	sub=''
	message=f'Subject: {sub}\n\n Hi {temp[0]}\n {body}'
	s.sendmail('enteryouremail@smtp.com',temp[1],message)
	s.close()
while(True):
	urls=open('link_conf.pkl','rb')
	data=pickle.load(urls)
	for i in range(len(data)):
		check(data[i][0],data[i][1])
	urls.close()
	time.sleep(60*60*8)