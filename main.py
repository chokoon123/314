from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
import re
import pandas as pd

def get():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    actions = ActionChains(driver)

    list_codes = []
    list_disc = []
    
    driver.get('https://web.reg.tu.ac.th/registrar/class_info.asp?lang=en')
    web_link = "https://web.reg.tu.ac.th/registrar/"
    
    ele = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[1]/td[2]/table/tbody/tr[7]/td[2]/table/tbody/tr/td/font[3]/input"))
    )
    ele.click()
    first_tab = driver.current_window_handle
    driver.maximize_window()
    time.sleep(5)
    while True:
        try:
            extracted_texts = []
            time.sleep(1)

            rows = driver.find_elements(By.XPATH, "//tr[@valign='TOP']")
            for row in rows:
                link_element = row.find_element(By.XPATH, ".//a[contains(@onclick, 'window.open')]")
                
                onclick_attribute = link_element.get_attribute("onclick")

                # Use regex 
                url_pattern = re.search(r"window\.open\('([^']+)'", onclick_attribute)

                extracted_url = url_pattern.group(1)  
                pyperclip.copy(extracted_url)  
                extracted_texts.append(extracted_url)  

                # print(f"Extracted URL: {extracted_url}")

            time.sleep(5)
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])

            for i in extracted_texts:
                link = web_link+i
                # print(link)
                driver.get(link)
                time.sleep(3)           
           
                codes = driver.find_elements(By.XPATH, "/html/body/table[1]/tbody/tr/td[2]/table/tbody/tr[1]/td[1]/b/font")
                for code in codes:
                    a = code.text
                    # print(a)
                    list_codes.append(a)

                disc = driver.find_elements(By.XPATH, "/html/body/table[2]/tbody/tr/td[2]/font[2]")
                for i in disc:
                    a = i.text
                    # print(a)
                    list_disc.append(a)

            #next page
            driver.switch_to.window(first_tab)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            try:
                # พยายามคลิกที่ลิงก์ NEXT อันที่สอง (ถ้ามี)
                NEXT = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[1]/td[2]/font/font/font/table/tbody/tr[32]/td[2]/font/a[2]')
                NEXT.click()
            except :
                try:
                    # ถ้าไม่มีลิงก์ NEXT อันที่สอง ให้คลิกที่ลิงก์แรกแทน
                    driver.find_element(By.XPATH, '/html/body/table/tbody/tr[1]/td[2]/font/font/font/table/tbody/tr[32]/td[2]/font/a').click()
                except NoSuchElementException:
                    print("ไม่พบปุ่ม 'NEXT' บนหน้านี้")
        
        except:
            print("DONE  "*10)
            break  

    dict = {"course":list_codes,"description":list_disc}
    df = pd.DataFrame(dict)
    driver.quit()
    return df    

if __name__ == '__main__' :
    get()