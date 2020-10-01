import requests
from bs4 import BeautifulSoup as bs

years=['2018','2017','2016']
orgs=dict()
for year in years:
    page="https://summerofcode.withgoogle.com/archive/%s/organizations/"%(year)
    html=requests.get(page)
    soup=bs(html.text,"html.parser")
    orgs_list_initial=soup.find_all('h4',attrs={'class':"organization-card__name font-black-54"})
    orgs_list=[]
    for org in orgs_list_initial:
        orgs_list.append(org.text.strip())

    for org in orgs_list:
        add=int(year)-2019
        add*=add
        if(og in orgs):orgs[og]+=add
        else:orgs[org]=add
#print(orgs)
orgs_sorted=sorted(orgs.items(),reverse=True, key=lambda kv: kv[1])
for og in orgs_sorted:
    val=og[1]
    if(og[1]==14):
        print(og[0],"2019",2017,2016)
    elif(val==13):print(og[0],2019,2017)
    elif(val==9):print(og[0],2019)
    elif(val==10):print(og[0],2019,2016)
    elif(val==4):print(og[0],2017)
    elif(val==1):print(og[0],2016)
    elif(val==5):print(og[0],2019,2016)
    

