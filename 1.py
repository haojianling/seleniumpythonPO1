from selenium import webdriver
from selenium.webdriver.support import expected_conditions as es
import time
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest
import pytesseract
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()

driver.get("http://www.5itest.cn/register")
time.sleep(5)
a=driver.find_element_by_id("register-btn").text
print(a)
print(es.title_contains("注册"))
#element=driver.find_element_by_class_name("controls")
#es.visibility_of_all_elements_located(element)
for i in range(5):
    user_email=''.join(random.sample('1234567890abcdefg',5))+'@163.com'
    print(user_email)
#es.presence_of_all_elements_located
locator=(By.CLASS_NAME,"controls")
WebDriverWait(driver,10).until(es.visibility_of_all_elements_located(locator))
email_element=driver.find_element_by_id("register_email")
print(email_element.get_attribute("placeholder"))
email_element.send_keys("807206678@qq.com")
print(email_element.get_attribute("value"))
driver.find_element_by_id("register_nickname").send_keys("1")
driver.find_element_by_id("register_password").send_keys("1")
print(driver.find_element_by_id("register_nickname-error").text)

driver.save_screenshot("E:/impoc.png")
code_elem=driver.find_element_by_id("getcode_num")
print(code_elem.location)
left=code_elem.location['x']
top=code_elem.location['y']
right=code_elem.size['width']+left
height=code_elem.size['height']+top
im=Image.open("E:/impoc.png")
img=im.crop((left,top,right,height))
img.save("E:/impoc1.png")
time.sleep(5)
# user_elem=driver.find_elements_by_class_name("controls")[1]
# user_elem.find_element_by_class_name("form-control").send_keys("hhh")
# driver.find_element_by_name("password").send_keys("111111")
# driver.find_element_by_name("captcha_code").send_keys("111111")

# image=Image.open("E:/impoc1.png")
# text=pytesseract.image_to_string(image)
# print(text)
r = ShowapiRequest("http://route.showapi.com/184-4", "142568", "ba6ac2df392d4f259d35c3ee7bce20d2" )
r.addFilePara("image", r"E:/impoc1.png")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
res = r.post()
text=res.json()["showapi_res_body"]["Result"]
print(text)
driver.find_element_by_name("captcha_code").send_keys(text)

time.sleep(3)
driver.close()
