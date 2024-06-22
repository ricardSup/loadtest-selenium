from selenium import webdriver
from time import sleep
from multiprocessing import Process, current_process
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import datetime

options = webdriver.ChromeOptions()

options.add_argument('--headless')   
options.add_argument('--disable-extensions')   
options.add_argument('--disable-gpu')   
options.add_argument("--no-sandbox")   
options.add_argument("--window-size=1920,1080")   
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-software-rasterizer')

PATH = "C:\Program Files (x86)\chromedriver.exe"

username = "user1"
password = "password"

url = "http://los.confins.one/"

def OpenClickSearch():
    driver = webdriver.Chrome(executable_path=PATH,options=options)
    process_name = current_process().name
    print('\n======================================================\n')
    print('Process name: ' + str(process_name))
    print('\n======================================================\n')
    driver.get(url)
         
    tries_init = 150
    for i in range(tries_init):
      try:
         print('\nlooping ' + str(i) + ' in pageinit\n')
         pageinit=WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'/html/body/app-root/app-content-layout/div/app-login-page/section/div/div/div/div/div[2]/div/h5')))
      except Exception, e:
         if i < tries_init - 1: # i is zero indexed
            print('\nlooping-exception ' + str(i) + ' in pageinit\n')
            driver.refresh()
            continue
         else:
            print("\nException has been thrown. " + str(e) + '\n')
            driver.close()
      break
 
    logininput=WebDriverWait(driver,15).until(EC.presence_of_element_located((By.ID, "inputUser")))
    ActionChains(driver).move_to_element(logininput).perform()


    driver.find_element_by_id("inputUser").send_keys(username)
    driver.find_element_by_id("inputPass").send_keys(password)
    timestart = datetime.datetime.now().replace(microsecond=0)
    print('\n======================================================\n')
    print('Process name: ' + str(process_name) + ' START, ' + timestart.strftime("%H:%M:%S")) 
    print('\n======================================================\n')
    
    loginbtn=WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,'//button[text()="LOGIN"]')))
    ActionChains(driver).move_to_element(loginbtn).click(loginbtn).perform()

    rolepickinit=WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-rolepick/div/table/tbody/tr[5]/td[4]/a')))
    ActionChains(driver).move_to_element(rolepickinit).perform()

    rolepick=WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-rolepick/div/table/tbody/tr[5]/td[4]/a')))
    ActionChains(driver).move_to_element(rolepick).click(rolepick).perform()

    driver.implicitly_wait(3)

    for i in range(150):
      try:
         thingstodo = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-full-layout/div/div[2]/div/div/div/app-dash-board/div[1]/div[1]/lib-ucthingstodo/div/div/div/h4")))
      except:
         if driver.current_url == 'http://los.confins.one/Pages/Login':    
            rolepick=WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-rolepick/div/table/tbody/tr[5]/td[4]/a')))
            ActionChains(driver).move_to_element(rolepick).click(rolepick).perform()
            continue

    tries_thingstodo = 150
    for i in range(tries_thingstodo):
      try:
         print('\nlooping ' + str(i) + ' in dashboard\n')
         print driver.current_url
         thingstodo = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-full-layout/div/div[2]/div/div/div/app-dash-board/div[1]/div[1]/lib-ucthingstodo/div/div/div/h4")))
         if thingstodo.text == "":
            driver.refresh()
            continue
         else:
            break
      except Exception, e:
         if i < tries_thingstodo - 1: # i is zero indexed
            print('\nlooping-exception ' + str(i) + ' in dashboard\n')
            driver.refresh()
            continue
         else:
            print("\nException has been thrown. " + str(e) + '\n')
            driver.close()
      break
    
    menuinquiryinit=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/app-root/app-full-layout/div/div[1]/app-sidebar/div[2]/div[1]/ul/li[2]/a/i')))
    ActionChains(driver).move_to_element(menuinquiryinit).click(menuinquiryinit).perform()

    menuinquiry=WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'/html/body/app-root/app-full-layout/div/div[1]/app-sidebar/div[2]/div[1]/ul/li[2]/ul/li[7]/a')))
    ActionChains(driver).move_to_element(menuinquiry).click(menuinquiry).perform()

    searchbtn=WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//*[@id="formSearch"]/div/div/div[2]/form/div/button[2]')))
    ActionChains(driver).move_to_element(searchbtn).click(searchbtn).perform()
      
    tries_search = 150
    for i in range(tries_search):
      try:
         print('\nlooping' + str(i) + ' in result_search \n')
         element = WebDriverWait(driver, 20).until(
         EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-full-layout/div/div[2]/div/div/div/app-inquiry-paging/lib-ucpaging/div/lib-ucgridfooter/div/div[3]"))
         )
         if element.text == "":
            searchbtn=WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//*[@id="formSearch"]/div/div/div[2]/form/div/button[2]')))
            ActionChains(driver).move_to_element(searchbtn).click(searchbtn).perform()
         else:
            print(element.text)
      except Exception, e:
         if i < tries_search - 1: # i is zero indexed
            print('\nlooping-exception' + str(i) + ' in result_search \n')
            searchbtn=WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//*[@id="formSearch"]/div/div/div[2]/form/div/button[2]')))
            ActionChains(driver).move_to_element(searchbtn).click(searchbtn).perform()
            continue
         else:
            print("\nException has been thrown. " + str(e) + '\n')
            driver.close()
      break
    
    driver.close()
   
    timefinish = datetime.datetime.now().replace(microsecond=0)
    difftime = (timefinish - timestart)
    print('\n======================================================\n')
    print('\nProcess name: ' + str(process_name) + ' FINISHED, ' + timefinish.strftime("%H:%M:%S") + ', LAMA PROSES ')
    print(difftime)
    print('\n======================================================\n')
    
def runInParallel(*fns_params):
   proc = []
   counter = 1
   for fn in fns_params:
         p = Process(target=fn)
         p.start()
         proc.append(p)
         counter = counter + 1
   for p in proc:
      p.join()

if __name__ == '__main__':
    runInParallel(
      OpenClickSearch,
      OpenClickSearch,
      OpenClickSearch
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # #20
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch,
      # OpenClickSearch
      #40
    )