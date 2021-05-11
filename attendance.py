from selenium import webdriver
import sys
import os.path
import getpass
import ctypes
from selenium.webdriver.chrome.options import Options
from data import csaId,csbId

MessageBox = ctypes.windll.user32.MessageBoxW
subId = csaId
myemail = ""
mypasswword = ""
myclass="CSA"
if os.path.exists('moodle_creds.txt'):
    f = open("moodle_creds.txt", "r")
    myemail = f.readline()
    mypasswword = f.readline()
    myclass=f.readline()
else:
    print("Enter email: ")
    myemail = input()
    print("Enter password: ")
    mypasswword = getpass.getpass()
    print("Enter your class (CSA/CSB): ")
    myclass = input().upper()
    f = open('moodle_creds.txt', 'w')
    f.write(myemail+'\n')
    f.write(mypasswword+'\n')
    f.write(myclass)
    print("Your email and password will be remembered. To change it, edit /moodle_creds.txt\n")
if myclass=="CSB":
    subId=csbId
else:
    subId=csaId
options =Options()
options.add_experimental_option('excludeSwitches', ['enable-logging']) #to avoid unwanted messaged being printed
options.headless =True #to run chromedriver in bg
driver = webdriver.Chrome(options= options)
sub=""
if len(sys.argv)==1:
    print("Enter subject code: ")
    sub=input().upper()
else:
    sub = sys.argv[1].upper()
driver.get('http://moodle.mec.ac.in/mod/attendance/view.php?id=' +
           subId[sub])
username = driver.find_element_by_id('username')
username.send_keys(myemail.strip('\n'))
password = driver.find_element_by_id('password')
password.send_keys(mypasswword.strip('\n'))
loginbtn = driver.find_element_by_id('loginbtn')
loginbtn.click()
item = driver.find_elements_by_xpath(
    "//a[contains(text(),'Submit attendance')]")
if item == []:
    MessageBox(None, 'No attendance found for '+ sub, 'Attendance', 0)
    sys.exit("No Attendance")

else:
    item[0].click()
    present = driver.find_element_by_xpath(
        "//span[contains(text(),'Present')]")
    present.click()
    submit = driver.find_element_by_id('id_submitbutton')
    submit.click()
    print("Attendance marked")
    MessageBox(None, 'Attendance marked for '+ sub +' succefully', 'Attendance', 0)
