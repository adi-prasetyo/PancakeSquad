from selenium import webdriver
from datetime import date
from datetime import datetime, timedelta
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
from random import randint
from time import sleep

df = pd.read_excel('PancakeSquad.xlsx')
df['ID'] = df['ID'].astype('str')
df['ID'] = df['ID'].str.zfill(4)
df = df.set_index('ID').sort_index()

df['Background'] = df['Background'].str.split('\n').str[0]
df['Bunny'] = df['Bunny'].str.split('\n').str[0]
df['Clothes'] = df['Clothes'].str.split('\n').str[0]
df['Eyes'] = df['Eyes'].str.split('\n').str[0]
df['Mouth'] = df['Mouth'].str.split('\n').str[0]
df['Ear'] = df['Ear'].str.split('\n').str[0]
df['Hat'] = df['Hat'].str.split('\n').str[0]

#get all the attributes of the nfts

driver = webdriver.Chrome(executable_path="chromedriver.exe")

timeout = 5 # seconds

for x in range(4420, 10000):
    
    driver.get(f"https://pancakeswap.finance/nfts/collections/0x0a8901b0E25DEb55A87524f0cC164E9644020EBA/{x}")
    
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//div[@class='sc-gtsrHT fEwclX']"))    
        WebDriverWait(driver, timeout).until(element_present)    
    except:
        driver.refresh()
        sleep(10)
    
    #wait = WebDriverWait(driver, timeout)
    #result = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='sc-gtsrHT fEwclX']")))
    
    result = driver.find_elements_by_xpath("//div[@class='sc-jSFjdj sc-gKAaRy kJmatq togOu']")  
    
    df.loc[x, 'ID'] = x
    
    try:
        df.loc[x, 'Background'] = result[1].text
    except:
        driver.refresh()
        sleep(5)
        df.loc[x, 'Background'] = result[1].text
        
    df.loc[x, 'Bunny'] = result[2].text
    df.loc[x, 'Clothes'] = result[3].text
    df.loc[x, 'Eyes'] = result[4].text
    df.loc[x, 'Mouth'] = result[5].text
    df.loc[x, 'Ear'] = result[6].text
    df.loc[x, 'Hat'] = result[7].text

    try:
        price_path = driver.find_elements_by_xpath("//div[@class='sc-gtsrHT jDnmwq']")
        price = price_path[4].text
    except:
        price = 'Not for sale'

    df.loc[x, 'Price (BNB)'] = price
    
    #there's often a random timeout, dont know if this random wait will fix it
    sleep(randint(5,10))