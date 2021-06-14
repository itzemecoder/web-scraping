driver = webdriver.Chrome('C:\\Users\\DELL\\Downloads\\chromedriver_win32\\chromedriver')


driver.get("https://www.glassdoor.co.in/index.html")
driver.maximize_window()



WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div/div/div[1]/article/header/nav/div[2]/div/div/div/button'))).click()

WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="userEmail"]'))).send_keys('shubham.pragroot@gmail.com')
WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="userPassword"]'))).send_keys("875596abc")
# WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div/div/div[1]/article/header/nav/div[2]/div/div/div/button'))).click()

driver.find_element_by_xpath('//*[@id="userPassword"]').send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element_by_id('sc.keyword').send_keys("Data Scientist")
# driver.find_element_by_xpath('//*[@id="sc.location"]').clear()
for i in range(0,10):
    driver.find_element_by_xpath('//*[@id="sc.location"]').send_keys(Keys.BACKSPACE)
driver.find_element_by_xpath('//*[@id="sc.location"]').send_keys("noida")
driver.find_element_by_xpath('//*[@id="sc.location"]').send_keys(Keys.ENTER)
time.sleep(20)
res = driver.page_source
soup = BeautifulSoup(res, 'html.parser')
name_of_com=soup.find_all('div',{'class':'d-flex flex-column pl-sm css-1d3xmk8 e1rrn5ka4'})
for name_of_com in name_of_com:
    name=name_of_com.find_all('span')
    print(name[0].text)
days_ago=soup.find_all('div',{'class':'d-flex align-items-end pl-std css-mi55ob'})    
for days in days_ago:
    print(days.text) 
rating=soup.find_all('span',{'class','css-19pjha7 e1cjmv6j1'})
for rat in rating:
    print(rat.text)    
    