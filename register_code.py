from selenium import webdriver
import time
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest
driver=webdriver.Firefox()
def driver_init():
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()
    time.sleep(5)

def get_element(id):
    element=driver.find_element_by_id(id)
    return element

def get_range_user():
    user_info=''.join(random.sample('1234567890abcdefg',8))
    return user_info

def get_code_image(file_name):
    driver.save_screenshot(file_name)
    code_elem = driver.find_element_by_id("getcode_num")
    print(code_elem.location)
    left = code_elem.location['x']
    top = code_elem.location['y']
    right = code_elem.size['width'] + left
    height = code_elem.size['height'] + top
    im = Image.open(file_name)
    img = im.crop((left, top, right, height))
    img.save(file_name)

def code_online(file_name):
    r = ShowapiRequest("http://route.showapi.com/184-4", "142568", "ba6ac2df392d4f259d35c3ee7bce20d2")
    r.addFilePara("image", file_name)
    r.addBodyPara("typeId", "35")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    res = r.post()
    text = res.json()["showapi_res_body"]["Result"]
    return text

def run_main():
    user_name_info=get_range_user()
    user_email=user_name_info+'@163.com'
    file_name="E:/image1.png"
    driver_init()
    get_element("register_email").send_keys(user_email)
    get_element("register_nickname").send_keys(user_name_info)
    get_element("register_password").send_keys("111111")
    get_code_image(file_name)
    text=code_online(file_name)
    get_element("captcha_code").send_keys(text)
    time.sleep(5)
    get_element("register-btn").click()
    driver.close()


run_main()