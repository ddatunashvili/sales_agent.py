from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import numpy as np
from playsound import playsound
# unidecode georgian
from unidecode import unidecode

'''
> შესვლა ვებსაიტზე
> პროდუქტების მოძებნა
> მათი ფასების/ რაოდენობის წამოღება 
> შენახვა/დალაგება მონაცემების
> საშუალო/მინ/მაქსის დათვლა
'''




# agent creating
agent = webdriver. Chrome(r'C:\Users\gio\Desktop\chatbot.py\chromedriver.exe')
# window minimazed
agent.set_window_position(-20000, 0)
# go to
keys=['პოპკორნის აპარატი','სენდვიჩერი','ფრის აპარატი','ხორცის საჭრელი','ელექტრო მაყალი','რძის ასაქაფებელი', 'ტოსტერი','წვენსაწური','ყინულის აპარატი','ნაყინის']
amount={}
products={}
# search each product
for key in keys:
    products[unidecode(key)]=[]
    agent.get('https://www.mymarket.ge/ka/?beta=2')
    search=agent.find_element_by_id('search-input').send_keys(key)
    button=agent.find_element_by_class_name('search-button').click()
    time.sleep(2)
    # get count
    content_count= agent.find_element_by_id('content-count')
    text=content_count.text
    amount[unidecode(key)]=[unidecode(text)]
    # get prices
    for i in range(3):
        prices=agent.find_elements_by_class_name('product-price')
        for price in prices:
            price=price.text
            price=float(price)
            # store price/ count
            products[unidecode(key)].append(price)
        try:
            next=agent.find_element_by_xpath('//*[@id="search-container"]/div[2]/nav/ul/a').click()
            time.sleep(2)
        except Exception as e:
            break
# calculate min / max /average
for product in products:
    list=products.get(product)
    list = [int(i) for i in list]
    average=sum(list) / len(list)
    min=np.min(list)
    max=np.max(list)
    print('=======================================')
    print(product,'sashualoa',average)
    print(min,'minimaluria',max,'maqsimaluria')
#    finish sound
    playsound(r'C:\Users\gio\Desktop\agent.py\fart.mp3')
