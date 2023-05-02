import requests
import pandas
from bs4 import BeautifulSoup

response=requests.get('https://shopping.yahoo.com/category/362/Surveillance-Cameras?merchants=3719d8d4-5edd-4817-998a-91f3229e7323&orderBy=DESC&renderBySimilarity=1&sortBy=popularity&spellCheck=1')
#print(response)

cams=BeautifulSoup(response.content,'html.parser')
#print(cams)


names=cams.find_all('span',class_="FluidProductCell__Title-sc-fsx0f7-9 gugkEY ellipsis_multi_2")
name=[]
for i in names[0:13]:
    x=i.get_text()
    name.append(x)
#print(name)  

links=cams.find_all('a',class_="unstyled-link")  
link=[]
for i in links[0:13]:
    x='https://shopping.yahoo.com/'+i['href']
    link.append(x)
#print(link)    


prices=cams.find_all('div',class_="FluidProductCell__PriceInfoWrap-sc-fsx0f7-13 gIXUJj")  
price=[]
for i in prices[0:13]:
    x=i.get_text()
    price.append(x)
#print(price)    


storename=cams.find_all('span',class_="FluidProductCell__MerchantInfo-sc-fsx0f7-8 nppFj ellipsis")  
store=[]
for i in storename[0:13]:
    x=i.get_text()
    store.append(x)
#print(store) 
   
data={'names':pandas.Series(name),
      'links':pandas.Series(link),
      'prices':pandas.Series(price),
      'storename':pandas.Series(store)}

cam=pandas.DataFrame(data)
cam.to_csv('cameras_data.csv')

