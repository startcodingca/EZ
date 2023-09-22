import requests
import pandas as pd
from bs4 import BeautifulSoup

urls = [
    "https://www.investing.com/equities/apple-computer-inc"
]
header = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0"}

res = requests.get(urls[0], headers=header)
print(res.text)
soup = BeautifulSoup(res.text, 'lxml')

price = soup.find("h1", {"class": "text-5xl/9 font-bold md:text-[42px] md:leading-[60px] text-[#232526]"})
name = soup.find("h1", {"class": "text-xl text-left font-bold leading-7 md:text-3xl md:leading-8 mb-2.5 md:mb-2 text-["
                                 "#232526] rtl:soft-ltr"})
print(price, name)'
