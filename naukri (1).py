from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import action_chains



import time

driver = webdriver.Firefox()
driver.maximize_window()
#driver.get("https://www.naukri.com/")


## QUESTION #1
def questionone():
    driver.get("https://www.naukri.com/")
    skillname = driver.find_element_by_xpath("//input[@id='qsb-keyword-sugg']")
    skillname.send_keys("Data Analyst")
    location = driver.find_element_by_xpath("//input[@id='qsb-location-sugg']")
    location.send_keys("Bangalore")
    # click the submit button
    searchbtn = driver.find_element_by_xpath("//button[@class='btn']")
    #searchBtn = driver.find_element_by_class_name("//search-btn")
    searchbtn.click()

    time.sleep(4)
    # Scrape 10 jobs: job-title, job-location, company_name, experience_required
    # /article[@class='jobTuple bgWhite br4 mb-8']
    joblist = driver.find_elements_by_xpath("//article[@class='jobTuple bgWhite br4 mb-8']")
    #print("Job is: ",joblist[1].find_element_by_xpath("//div[@class='jobTupleHeader']/div[@class='info fleft']/a[@class='title fw500 ellipsis']").get_attribute("title"))
    jobtitle = driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
    #print("Job 1: ", jobtitle[3].get_attribute("text"))
    companyname = driver.find_elements_by_xpath("//a[@class='subTitle ellipsis fleft']")


    joblocation = driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']/span[@class='ellipsis fleft fs12 lh16']")

    experiencerequired = driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi experience']/span[@class='ellipsis fleft fs12 lh16']")
    print("experience requried: ", experiencerequired)


    counter = 0
    for title in jobtitle:
        #x = job.find_element_by_xpath("//a[@class='subTitle ellipsis fleft']")
        if(counter == 10):
            break
        else:
            print(counter, ": " , title.get_attribute("text"))
        counter += 1
    
    counter = 0
    for company in companyname:
        if(counter == 10):
            break
        else:
            print(counter, ": " ,company.get_attribute("text")) 
        counter += 1

    counter = 0
    for loc in joblocation:
        if(counter == 10):
            break
        else:
            print(counter, ": " , loc.get_attribute("title")) 
        counter += 1

    counter = 0
    for exp in experiencerequired:
        if(counter == 10):
            break
        else:
            print(counter, ": " , exp.get_attribute("title")) 
        counter += 1


def questionthree():
    skillname = driver.find_element_by_xpath("//input[@id='qsb-keyword-sugg']")
    skillname.send_keys("Data Scientist")
    # click the submit button
    searchbtn = driver.find_element_by_xpath("//button[@class='btn']")
    #searchBtn = driver.find_element_by_class_name("//search-btn")
    searchbtn.click()
    time.sleep(4)

    # click the filters
    #button = driver.find_element_by_xpath("//input[@id='chk-3-6 Lakhs-ctcFilter-']/label[@class='chkLbl']").click()
    #driver.find_element_by_css_selector('i.fleft.naukicon.naukicon-checkbox').click(); 
    driver.find_element_by_xpath("//label[@for='chk-3-6 Lakhs-ctcFilter-']/i[@class='fleft naukicon naukicon-checkbox']").click();
    time.sleep(3)

    driver.find_element_by_xpath("//label[@for='chk-Delhi / NCR-cityTypeGid-']/i[@class='fleft naukicon naukicon-checkbox']").click();
    time.sleep(3)

    jobtitle = driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
    #print("Job 1: ", jobtitle[3].get_attribute("text"))
    companyname = driver.find_elements_by_xpath("//a[@class='subTitle ellipsis fleft']")


    joblocation = driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']/span[@class='ellipsis fleft fs12 lh16']")

    experiencerequired = driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi experience']/span[@class='ellipsis fleft fs12 lh16']")
    print("experience requried: ", experiencerequired)

    counter = 0
    for title in jobtitle:
        #x = job.find_element_by_xpath("//a[@class='subTitle ellipsis fleft']")
        if(counter == 10):
            break
        else:
            print(counter, ": " , title.get_attribute("text"))
        counter += 1
    
    counter = 0
    for company in companyname:
        if(counter == 10):
            break
        else:
            print(counter, ": " ,company.get_attribute("text")) 
        counter += 1

    counter = 0
    for loc in joblocation:
        if(counter == 10):
            break
        else:
            print(counter, ": " , loc.get_attribute("title")) 
        counter += 1

    counter = 0
    for exp in experiencerequired:
        if(counter == 10):
            break
        else:
            print(counter, ": " , exp.get_attribute("title")) 
        counter += 1



def question_four():
    driver.get("https://www.glassdoor.co.in/index.html")

def question_six():
    driver.get("https://www.flipkart.com")
    driver.find_element_by_xpath("//button[@class='_2KpZ6l _2doB4z']").click()

    query = driver.find_element_by_xpath("//input[@class='_3704LK']")
    query.send_keys("sunglasses")
    driver.find_element_by_xpath("//button[@class='L0Z3Pu']").click()

    time.sleep(20)

    # brand, product desc, price, discount
    brand = driver.find_elements_by_xpath("//div[@class='_2WkVRV']")
    print(len(brand))
    pro_desc = driver.find_elements_by_xpath("//a[@class='IRpwTa _2-ICcC']")
    price = driver.find_elements_by_xpath("//div[@class='_30jeq3']")
    discount = driver.find_elements_by_xpath("//div[@class='_3Ay6Sb']/span")

    list_brand = []
    list_desc = []
    list_price = []
    list_discount = []

    # PAGE 1
    counter = 1
    for b in brand:
        print(counter, ": ", b.text)
        list_brand.append(b.text)
        counter += 1

    # PAGE 2: click the next button
    driver.find_element_by_xpath("//a[@class='_1LKTO3']").click()
    time.sleep(15)
    brand = driver.find_elements_by_xpath("//div[@class='_2WkVRV']")
    for b in brand:
        if counter == 101:
            break
        else:
            print(counter, ": ", b.text)
            list_brand.append(b.text)
        counter += 1

    # PAGE 3: click the next button
    driver.find_element_by_xpath("//a[@class='_1LKTO3']").click()
    time.sleep(15)
    brand = driver.find_elements_by_xpath("//div[@class='_2WkVRV']")
    for b in brand:
        if counter == 101:
            break
        else:
            print(counter, ": ", b.text)
            list_brand.append(b.text)
        counter += 1

    ## DESCRIPTION

    counter = 1
    driver.get("https://www.flipkart.com/search?q=sunglasses&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=1")
    pro_desc = driver.find_elements_by_xpath("//a[@class='IRpwTa']")
    print("len: ", len(pro_desc))
    for desc in pro_desc:
        print(counter, ": ", desc.get_attribute("title"))
        list_desc.append(desc.get_attribute("title"))
        counter += 1

    #page 2
    driver.find_element_by_xpath("//a[@class='_1LKTO3']").click()
    time.sleep(15)
    pro_desc = driver.find_elements_by_xpath("//a[@class='IRpwTa']")
    print("len: ", len(pro_desc))
    for desc in pro_desc:
        print(counter, ": ", desc.get_attribute("title"))
        list_desc.append(desc.get_attribute("title"))
        counter += 1

    #page 3
    driver.find_element_by_xpath("//a[@class='_1LKTO3']").click()
    time.sleep(15)
    pro_desc = driver.find_elements_by_xpath("//a[@class='IRpwTa']")
    print("len: ", len(pro_desc))
    for desc in pro_desc:
        if counter == 101:
            break
        else:
            print(counter, ": ", desc.get_attribute("title"))
            list_desc.append(desc.get_attribute("title"))
        counter += 1

    ## PRICE

    counter = 1
    driver.get("https://www.flipkart.com/search?q=sunglasses&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=1")
    price = driver.find_elements_by_xpath("//div[@class='_30jeq3']")
    print("len: ", len(pro_desc))
    for p in price:
        print(counter, ": ", p.text)
        list_price.append(p.text)
        counter += 1

    #page 2
    driver.find_element_by_xpath("//a[@class='_1LKTO3']").click()
    time.sleep(15)
    price = driver.find_elements_by_xpath("//div[@class='_30jeq3']")
    print("len: ", len(pro_desc))
    for p in price:
        print(counter, ": ", p.text)
        list_price.append(p.text)
        counter += 1

    #page 3
    driver.find_element_by_xpath("//a[@class='_1LKTO3']").click()
    time.sleep(15)
    price = driver.find_elements_by_xpath("//div[@class='_30jeq3']")
    print("len: ", len(price))
    for p in price:
        if counter == 101:
            break
        else:
            print(counter, ": ", p.text)
            list_price.append(p.text)
        counter += 1


    ## DISCOUNT

    counter = 1
    driver.get("https://www.flipkart.com/search?q=sunglasses&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=1")
    discount = driver.find_elements_by_xpath("//div[@class='_3Ay6Sb']/span")
    print("len: ", len(discount))
    for dis in discount:
        print(counter, ": ", dis.text)
        list_discount.append(dis.text)
        counter += 1

    #page 2
    driver.find_element_by_xpath("//a[@class='_1LKTO3']").click()
    time.sleep(15)
    discount = driver.find_elements_by_xpath("//div[@class='_3Ay6Sb']/span")
    print("len: ", len(pro_desc))
    for dis in discount:
        print(counter, ": ", dis.text)
        list_discount.append(dis.text)
        counter += 1

    #page 3
    driver.find_element_by_xpath("//a[@class='_1LKTO3']").click()
    time.sleep(15)
    discount = driver.find_elements_by_xpath("//div[@class='_3Ay6Sb']/span")
    print("len: ", len(pro_desc))
    for dis in discount:
        if counter == 101:
            break
        else:
            print(counter, ": ", dis.text)
            list_discount.append(dis.text)
        counter += 1




def question_eight():
    driver.get("https://www.flipkart.com")
    driver.find_element_by_xpath("//button[@class='_2KpZ6l _2doB4z']").click()

    query = driver.find_element_by_xpath("//input[@class='_3704LK']")
    query.send_keys("sneakers")
    driver.find_element_by_xpath("//button[@class='L0Z3Pu']").click()

    time.sleep(20)

    # brand, product desc, price, discount
    brand = driver.find_elements_by_xpath("//div[@class='_2WkVRV']")
    print(len(brand))
    pro_desc = driver.find_elements_by_xpath("//a[@class='IRpwTa _2-ICcC']")
    price = driver.find_elements_by_xpath("//div[@class='_30jeq3']")
    discount = driver.find_elements_by_xpath("//div[@class='_3Ay6Sb']/span")

    list_brand = []
    list_desc = []
    list_price = []
    list_discount = []

    # PAGE 1
    counter = 1
    for b in brand:
        print(counter, ": ", b.text)
        list_brand.append(b.text)
        counter += 1

    # PAGE 2: click the next button
    driver.find_element_by_xpath("//a[@class='_1LKTO3']").click()
    time.sleep(15)
    brand = driver.find_elements_by_xpath("//div[@class='_2WkVRV']")
    for b in brand:
        if counter == 101:
            break
        else:
            print(counter, ": ", b.text)
            list_brand.append(b.text)
        counter += 1

    # PAGE 3: click the next button
    driver.find_element_by_xpath("//a[@class='_1LKTO3']").click()
    time.sleep(15)
    brand = driver.find_elements_by_xpath("//div[@class='_2WkVRV']")
    for b in brand:
        if counter == 101:
            break
        else:
            print(counter, ": ", b.text)
            list_brand.append(b.text)
        counter += 1

    ## DESCRIPTION

    counter = 1
    driver.get("https://www.flipkart.com/search?q=sneakers&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=1")
    pro_desc = driver.find_elements_by_xpath("//a[@class='IRpwTa']")
    print("len: ", len(pro_desc))
    for desc in pro_desc:
        print(counter, ": ", desc.get_attribute("title"))
        list_desc.append(desc.get_attribute("title"))
        counter += 1

    #page 2
    driver.find_element_by_xpath("//a[@class='_1LKTO3']").click()
    time.sleep(15)
    pro_desc = driver.find_elements_by_xpath("//a[@class='IRpwTa']")
    print("len: ", len(pro_desc))
    for desc in pro_desc:
        print(counter, ": ", desc.get_attribute("title"))
        list_desc.append(desc.get_attribute("title"))
        counter += 1

    #page 3
    driver.find_element_by_xpath("//a[@class='_1LKTO3']").click()
    time.sleep(15)
    pro_desc = driver.find_elements_by_xpath("//a[@class='IRpwTa']")
    print("len: ", len(pro_desc))
    for desc in pro_desc:
        if counter == 101:
            break
        else:
            print(counter, ": ", desc.get_attribute("title"))
            list_desc.append(desc.get_attribute("title"))
        counter += 1

    ## PRICE

    counter = 1
    driver.get("https://www.flipkart.com/search?q=sneakers&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=1")
    price = driver.find_elements_by_xpath("//div[@class='_30jeq3']")
    print("len: ", len(pro_desc))
    for p in price:
        print(counter, ": ", p.text)
        list_price.append(p.text)
        counter += 1

    #page 2
    driver.find_element_by_xpath("//a[@class='_1LKTO3']").click()
    time.sleep(15)
    price = driver.find_elements_by_xpath("//div[@class='_30jeq3']")
    print("len: ", len(pro_desc))
    for p in price:
        print(counter, ": ", p.text)
        list_price.append(p.text)
        counter += 1

    #page 3
    driver.find_element_by_xpath("//a[@class='_1LKTO3']").click()
    time.sleep(15)
    price = driver.find_elements_by_xpath("//div[@class='_30jeq3']")
    print("len: ", len(price))
    for p in price:
        if counter == 101:
            break
        else:
            print(counter, ": ", p.text)
            list_price.append(p.text)
        counter += 1


    ## DISCOUNT

    counter = 1
    driver.get("https://www.flipkart.com/search?q=sneakers&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=1")
    discount = driver.find_elements_by_xpath("//div[@class='_3Ay6Sb']/span")
    print("len: ", len(discount))
    for dis in discount:
        print(counter, ": ", dis.text)
        list_discount.append(dis.text)
        counter += 1

    #page 2
    driver.find_element_by_xpath("//a[@class='_1LKTO3']").click()
    time.sleep(15)
    discount = driver.find_elements_by_xpath("//div[@class='_3Ay6Sb']/span")
    print("len: ", len(pro_desc))
    for dis in discount:
        print(counter, ": ", dis.text)
        list_discount.append(dis.text)
        counter += 1

    #page 3
    driver.find_element_by_xpath("//a[@class='_1LKTO3']").click()
    time.sleep(15)
    discount = driver.find_elements_by_xpath("//div[@class='_3Ay6Sb']/span")
    print("len: ", len(pro_desc))
    for dis in discount:
        if counter == 101:
            break
        else:
            print(counter, ": ", dis.text)
            list_discount.append(dis.text)
        counter += 1



def question_nine():
    driver.get("https://www.myntra.com/shoes")
    price_list = driver.find_elements_by_xpath("//div[@class='common-checkboxIndicator']")
    #price_list = price_list.find_elements_by_xpath("/label[@class='common-customCheckbox vertical-filters-label']")
    print("Len of price_list = ", len(price_list))
    price_list[15].click()
    time.sleep(5)
    #price_list[1].find_element_by_xpath("//div[@class='common-checkboxIndicator']").click()
    # div.common-checkboxIndicator
    color_list = driver.find_elements_by_xpath("//ul/li[@class='colour-listItem']")
    print("Len of color_list = ", len(color_list))
    color_list[0].find_element_by_xpath("//label[@class='common-customCheckbox']").click()

    time.sleep(5)
    # brand, desc, prices
    brands = driver.find_elements_by_xpath("//h3[@class='product-brand']")
    prices = driver.find_elements_by_xpath("//div[@class='product-price']")

    counter = 1
    for brand in brands:
        print(counter, ": ", brand.text)
        counter += 1

    driver.find_element_by_xpath("//a[@rel='next']").click()
    time.sleep(5)
 
    brands = driver.find_elements_by_xpath("//h3[@class='product-brand']")
    for brand in brands:
        print(counter, ": ", brand.text)
        counter += 1


    driver.find_element_by_xpath("//a[@rel='prev']").click()
    time.sleep(5)

    descs = driver.find_elements_by_xpath("//h4[@class='product-product']")
    counter = 1
    for desc in descs:
        print(counter, ": ", desc.text)
        counter += 1

    driver.find_element_by_xpath("//a[@rel='next']").click()
    time.sleep(5)
 
    descs = driver.find_elements_by_xpath("//h4[@class='product-product']")
    for desc in descs:
        print(counter, ": ", desc.text)
        counter += 1


    driver.find_element_by_xpath("//a[@rel='prev']").click()
    time.sleep(5)
    prices = driver.find_elements_by_xpath("//div[@class='product-price']")
    print("Len of prices: ", len(prices))
    for price in prices:
        try:
            print(price.find_element_by_class_name("product-discountedPrice").text)
        except:
            print(price.find_element_by_tag_name("span").text)

    driver.find_element_by_xpath("//a[@rel='next']").click()
    time.sleep(5)
    prices = driver.find_elements_by_xpath("//div[@class='product-price']")
    for price in prices:
        try:
            print(price.find_element_by_class_name("product-discountedPrice").text)
        except:
            print(price.find_element_by_tag_name("span").text)


#//*[@id="desktopSearchResults"]/div[2]/section/ul/li[1]/a/div[2]/div[1]/span[1]/span[1]
#//*[@id="desktopSearchResults"]/div[2]/section/ul/li[2]/a/div[2]/div[1]/span


questionone()
#questionthree()
#question_eight()

#question_nine()
