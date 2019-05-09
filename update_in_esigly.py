
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import os 
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import lxml
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
url = 'https://esig.ly'
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get(url + '/login')

def getElById(value):
        return driver.find_element_by_id(str(value))

def loginUser(obj,value):
    return obj.send_keys(str(value))
loginDict = {
 'username': {
     'field': getElById('username'),
     'value': '' 
     },
  'pass': {
      'field': getElById('password'),
      'value': ''
  }
}
for element in loginDict:
    try:
        loginUser(loginDict[element]['field'], loginDict[element]['value'])
    except:
        print(Exception)
login_button = driver.find_element_by_css_selector('body > div.container.ng-scope > div.login_left > div.account_options > form > fieldset > div:nth-child(3) > div > button')
login_button.click()
sleep(10)
#driver.get(url + '/signatures')

result_size = Select(driver.find_element_by_xpath('//*[@id="content"]/section/section/footer/div/div[1]/select'))
result_size.select_by_index(4)
sleep(5)
soup = BeautifulSoup(driver.page_source,'lxml')
rows = soup.find_all('tr', class_='ng-scope')
cnt = 2
for i, row in enumerate(rows):
    if i<=174:
        print(i)
        cnt = cnt + 1

    else:    
        sleep(3)
        id_td =  row.find('td',class_="sig_id hide_767").text
        name_td = row.find('td', class_="sig_name max_100 no-wrap ng-binding").text
        name = name_td.title()
        position_td = row.find('td', class_="sig_role hide_1800 max_100 no-wrap ng-binding").text
    
        email_link = driver.find_element_by_xpath('//*[@id="content"]/section/section/div[3]/table/tbody/tr[%d]/td[7]/a[1]'%(cnt,))
        delete_link = driver.find_element_by_xpath('//*[@id="content"]/section/section/div[3]/table/tbody/tr[%d]/td[8]/a'%(cnt,))
        sleep(2)
        actions = ActionChains(driver)
        actions.move_to_element(email_link)
        actions.click(email_link)
        actions.perform()
        actions.reset_actions()
        no_button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div/div/button[2]')
        soup2 = BeautifulSoup(driver.page_source,'lxml')
        email_link = soup2.find('p', class_="ng-binding")
        email_text = email_link.text
        email_regex = re.compile('\S+@gpg.com')
        email = email_regex.findall(email_text)
        action_move = ActionChains(driver)
        action_move.move_to_element(no_button)
        action_move.click(no_button)
        action_move.perform()
        action_move.reset_actions()
        sleep(8)
        duplicate_link = driver.find_element_by_xpath('//*[@id="content"]/section/section/div[3]/table/tbody/tr[%d]'%(cnt,))
        
        action2 = ActionChains(driver)
        action2.move_to_element(duplicate_link)
        action2.click(duplicate_link)
        #action2.click(duplicate_link)
        action2.perform()
        action2.reset_actions()
       
       
       
        sleep(2)
        driver.implicitly_wait(2)

        name_field = driver.find_element_by_xpath('//*[@id="name"]')
        role_field = driver.find_element_by_xpath('//*[@id="role"]')
        email_field = driver.find_element_by_xpath('//*[@id="email"]')
        for char in name:
            name_field.send_keys(char)
        name_field.clear()
        for char in name:
            name_field.send_keys(char)

        role_field.send_keys(position_td)
        email_field.send_keys(email)

        action_dup = ActionChains(driver)
        duplicate_button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[1]/form/div[5]/button[1]')
        action_dup.move_to_element(duplicate_button)
        close_item = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/button')
        action_dup.key_down(Keys.COMMAND)
        action_dup.click(duplicate_button)
        action_dup.move_to_element(close_item)
        action_dup.click(close_item)
        action_dup.perform()
        action_dup.reset_actions()
        

        sleep(10)
        
        action_remove = ActionChains(driver)
        action_remove.move_to_element(delete_link)
        action_remove.click(delete_link)
        action_remove.perform()
        action_remove.reset_actions()
        sleep(1)
        confirm_remove = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div/div/button[1]')
        action_confirm_remove = ActionChains(driver)
        action_confirm_remove.move_to_element(confirm_remove)
        action_confirm_remove.click(confirm_remove)
        action_confirm_remove.perform()
        action_confirm_remove.reset_actions()
        sleep(10)
        cnt = cnt + 1



#close /html/body/div[1]/div/div/div/button
#duplicate /html/body/div[1]/div/div/div/div/div[1]/form/div[5]/button[1]/strong[1]
# delete //*[@id="content"]/section/section/div[3]/table/tbody/tr[2]/td[8]/a
# confirm delete /html/body/div[1]/div/div/div/div/div/div/div/button[1]
#driver.execute_script(openModal(70267,40))







# 