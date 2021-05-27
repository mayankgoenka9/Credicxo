#Install selenium - pip install selenium
import json
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

""" 
No proxy was available at the time of testing

def get_free_proxies():
    url = "http://www.freeproxylists.net/"
    proxies=[]
    driver_path = "C:\Projects\selenium_dev\Credicxo\chromedriver.exe"
    driver=webdriver.Chrome(driver_path)
    driver.get(url)
    country=Select(driver.find_element_by_xpath("//*[@id='form1']/table/tbody/tr[2]/td[1]/select"))
    country.select_by_value('US')
    time.sleep(1)
    select=driver.find_element_by_xpath("//*[@id='form1']/table/tbody/tr[3]/td/input")
    select.click()
    time.sleep(3)
    table = driver.find_element_by_xpath("/html/body/div[1]/div[2]/table")
    tr = table.find_elements_by_tag_name("tr")
    tr.pop(0)
    for row in tr:
        tds = row.find_elements_by_tag_name("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            proxies.append(str(ip) + ":" + str(port))
        except IndexError:
            continue
    return proxies

url = "http://httpbin.org/ip"
proxies = get_free_proxies()

for i in range(len(proxies)):

    #printing req number
    print("Request Number : " + str(i+1))
    proxy = proxies[i]
    try:
        response = requests.get(url, proxies = {"http":proxy, "https":proxy})
        print(response.json())
    except:
        # if the proxy Ip is pre occupied
        print("Not Available")


"""
# we are starting with page one, and continue until last page
page=1
url=f"https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage={page}"
# specify path of browser driver file
driver_path = "C:\Projects\selenium_dev\Credicxo\chromedriver.exe"
# initializing driver
driver = webdriver.Chrome(driver_path)
driver.get(url)
# list to store price,title,stock_status,manufacturer in form of dictionaries
scraped=[]
# driver code
try:
    # using while loop to scrape every product till last page
    while True:
        # we have to wait until the page loads required element
        prods_cont = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-container"))
        )
        # prods is list of all products
        prods=prods_cont.find_elements_by_id("Div1")
        # we will loop through each product, scrape it and update our scraped list simultaneously
        for prod in prods:
            title = prod.find_element_by_class_name("catalog-item-name")
            mnftr = prod.find_element_by_class_name("catalog-item-brand")
            price = prod.find_element_by_class_name("price")
            status = prod.find_element_by_class_name("status")
            if status.text=='Out of Stock':
                in_stock = False
            else:
                in_stock = True
            scraped.append(
                {
                    "price" : price.text,
                    "title" : title.text,
                    "stock" : in_stock,
                    "maftr" : mnftr.text
                }
            )
        # we will now find if there is a next page
        t=driver.find_element_by_xpath("/html/body/form/main/div/section/section/div[3]/div[1]/span/a[4]")
        # if there exists another page, we will update our url with page number incremented by 1,
        # and redirect our driver to that url and scrape till last page 
        if t.text=='Next':
            page+=1
            url=f"https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage={page}"
            driver.get(url)
        else:
            break
# finally update the json file and close the browser
finally:
    with open('C:/Projects/selenium_dev/Credicxo/task_result.json','w') as result:
        json.dump(scraped,result,indent=4)
    driver.quit()