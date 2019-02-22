
##scrapping in paytmmall.

###redmi note mobiles:

import requests
from bs4 import BeautifulSoup
# url="https://paytmmall.com/shop/search?q=redmi%20note&from=organic&child_site_id=6&site_id=2&category=66781&brand=18550"
# page=requests.get(url)
# parse=BeautifulSoup(page.text,"html.parser")
# main_div=parse.find("div", class_="_3RA-")
# div1=main_div.findAll("div", class_="_1fje")
# # print div1
# index=1
# for i in div1:
# 	# print i,"\n"
# 	div2=i.findAll("div", class_="_2i1r")
# 	# print div2
	
# 	for j in div2:

# 		div3=j.find("div",class_="_3WhJ")
# 		# print div3
# 		div4=div3.find("a")
# 		# print div4
# 		div5=div4.find("div",class_="pCOS")
# 		# print div5
# 		mobile_name=div5.find("div",class_="_2apC")
# 		# print div6.text
# 		div7=div5.find("div",class_="_2bo3")
# 		div8=div7.find("div",class_="_1kMS")
# 		price=div8.find("span")
# 		print (index,price.text,mobile_name.text)
# 		index=index+1

##DELL LAPTOPS 

link="https://paytmmall.com/laptops-glpid-6453?use_mw=1&page=1&brand=1758&src=store"
dell=requests.get(link)
# print (dell)
parser=BeautifulSoup(dell.text,"html.parser")
# print (parser)
main_div1=parser.find("div",class_="_3RA-")
# print (main_div1)
lap=main_div1.findAll("div",class_="_1fje")

for k in lap:
	lap1=k.findAll("div",class_="_2i1r")
	for m in lap1:
		lap2=m.find("div",class_="_3WhJ")
		a=lap2.find("a")
		lap3=a.find("div",class_="pCOS")
		name=lap3.find("div",class_="_2apC")

		lap4=lap3.find("div",class_="_2bo3")

		lap5=lap4.find("div",class_="_1kMS")
		print (lap5.text,name.text)

