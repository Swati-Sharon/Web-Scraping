#pip install requests-html
from requests_html import HTMLSession
session=HTMLSession()

query='New Delhi'

#getting url of the page of webscrapping
#formatting the url to put query element
url=f'https://www.google.com/search?q=weather+new+delhi+{query}'

#get 'user-agent' from browser searching "my user agent"
r=session.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'})

#title of page by default
#print(r.html.find('title',first=True).text)

#get the id
#div class.span id
temp=r.html.find('span#wob_tm',first=True).text

#div class span class
degree=r.html.find('div.vk_bk.wob-unit span.wob_t',first=True).text

#condition=r.html.find('div.VQF4g',first=True).find('span#wob_dc',first=True).text
condition=r.html.find('span#wob_dc',first=True).text

day_time=r.html.find('div.VQF4g',first=True).find('div#wob_dts',first=True).text

print(temp,degree,condition,day_time)
