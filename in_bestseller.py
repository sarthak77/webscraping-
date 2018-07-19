import csv
import requests
from bs4 import BeautifulSoup

#1 page
page=requests.get("https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_1?ie=UTF8&pg=1")
soup=BeautifulSoup(page.content,"html.parser")
allinfo=soup.find_all("div",{"class":"zg_itemWrapper"})

#2 page
page=requests.get("https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_1?ie=UTF8&pg=2")
soup=BeautifulSoup(page.content,"html.parser")
extra=soup.find_all("div",{"class":"zg_itemWrapper"})
for i in extra:
	allinfo.append(i)

#3 page
page=requests.get("https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_1?ie=UTF8&pg=3")
soup=BeautifulSoup(page.content,"html.parser")
extra=soup.find_all("div",{"class":"zg_itemWrapper"})
for i in extra:
	allinfo.append(i)

#4 page
page=requests.get("https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_1?ie=UTF8&pg=4")
soup=BeautifulSoup(page.content,"html.parser")
extra=soup.find_all("div",{"class":"zg_itemWrapper"})
for i in extra:
	allinfo.append(i)

#5 page
page=requests.get("https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_1?ie=UTF8&pg=5")
soup=BeautifulSoup(page.content,"html.parser")
extra=soup.find_all("div",{"class":"zg_itemWrapper"})
for i in extra:
	allinfo.append(i)

#a=1
#for i in range(100):
#	print("")
#	print("")
#	print("")
#	print(a)
#	print(allinfo[i])
#	a=a+1

#contains <a> tag
temp1=[]
for i in allinfo:
	temp1.append(i.find("a"))

#store url
url=[]
for i in temp1:
	url.append(i["href"])

#for i in url:
#	print (i)

#contains <div> inside <a> tag
temp2=[]
for i in temp1:
	temp2.append(i.find_all("div"))

#book contains book
book=[]
for i in temp2:
	book.append(i[1].get_text())

#for i in book:
#	print(i)

#temp3 contains <div> tags
temp3=[]
for i in allinfo:
	temp3.append(i.find_all("div"))

#a=1
#for i in temp3:
#	print(a)
#	print("")
#	print("")
#	print("")
#	print(i)
#	a=a+1

#author
author=[]
for i in temp3:
	if(len(i[5])>2):
		author.append("Not available")
	else:
		author.append(i[3].get_text())

#for i in author:
#	print(i)


#temp4 contains 7th div in allinfo
temp4=[]
for i in temp3:
	try:
		temp4.append(i[6])
	except:
		try:
			t1=i[5]
			temp4.append(t1.find_all("span")[1].get_text())
		except:
			temp4.append("Not available")


#price
price=[]
for i in temp4:
	try:
		price.append(i.find_all("span")[1].get_text())
	except:
		price.append(i)

#for i in price:
#	print(i)

#temp5 contains 6th div
temp5=[]
for i in temp3:
	if(len(i[5])>2):
		temp5.append(i[3])
	else:
		temp5.append(i[4])

#avg rating
avgrat=[]
for i in temp5:
	try:
		avgrat.append(i.find_all("a")[0].get_text())
	except:
		avgrat.append("Not available")


#for i in avgrat:
#	print(i)

#rating
rat=[]
for i in temp5:
	try:
		rat.append(i.find_all("a")[1].get_text())
	except:
		rat.append("Not available")

#for i in rat:
#	print(i)


finallist=[]
finallist.append(["Name","URL","Author","Price","Number of Ratings","Average Rating"])
for i in range(100):
	finallist.append([book[i].strip(),"https://www.amazon.in"+url[i].strip(),author[i].strip(),price[i].strip(),rat[i].strip(),avgrat[i].strip()])

#for i in finallist:
#	print(i[0])
#	print(i[1])
#	print(i[2])
#	print(i[3])
#	print(i[4])
#	print(i[5])

myfile=open("in_book.csv","w")
with myfile:
	writer=csv.writer(myfile,delimiter=";")
	writer.writerows(finallist)
