from selenium import webdriver
from time import sleep

#Remove all the number of friends you follow on Instagram 
#before running the tool. You have to download chromedriver browser * does not work on mobile devices *
#قم بإزالة كل عدد الأصدقاء الذين تتابعهم على انستغرام  قبل تشغيل الأداة. يجب عليك تنزيل متصفح كروم درايفر لا يعمل على الأجهزة المحمولة

ch = input("[*]Enter the >chromedriver< path: ")

driver = webdriver.Chrome(executable_path=f"{ch}")
driver.get("https://www.instagram.com/")
sleep(4)

user = input("[*]Enter user name: ")
driver.find_element_by_xpath("//input[@name=\"username\"]")\
    .send_keys(user)

passw = input("[*]Enter password: ")
unfollow = int(input("[*]How many friends do you want to remove?:"))
driver.find_element_by_xpath("//input[@name=\"password\"]")\
    .send_keys(passw)

driver.find_element_by_xpath("//button[@type=\"submit\"]")\
    .click()
sleep(4)


driver.get("https://www.instagram.com/"f"{user}/")
following = driver.find_element_by_partial_link_text("following")
following.click()
sleep(3)

for n in range(unfollow):
    driver.find_element_by_xpath('//button[text()="Following"]')\
        .click()
    driver.find_element_by_xpath('//button[text()="Unfollow"]')\
        .click()
    sleep(2)

