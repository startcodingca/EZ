import requests
from bs4 import BeautifulSoup
#soup = BeautifulSoup(html_doc, 'html.parser')
import pandas as pd

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; \
    Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/84.0.4147.105 Safari/537.36'}

urls = [
		'https://www.investing.com/equities/apple-computer-inc'
		]

page = requests.get(urls[0])

#200 means it was a success request
print(page.status_code)

soup = BeautifulSoup(page.text, 'html.parser')

company = soup.find('hi', {'class': 'text-xl text-left font-bold leading-7 md:text-3xl md:leading-8 mb-2.5 md:mb-2 text-[#232526] rtl:soft-ltr'}).text
price = soup.find('div', {'class': 'text-5xl/9 font-bold md:text-[42px] md:leading-[60px] text-[#232526]'}).text


print("URL:", urls[0])
print("Company:", company)
print("Price: $"+price)