from selenium import webdriver
import time
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest
from base.find_element import FindElement
class RegisterFunction(object):
    def __init__(self,url,i):
        self.driver=self.get_driver(url,i)
    def get_driver(self,url,i):
        if i==0:
            driver=webdriver.Firefox()
        elif i==1:
            driver=webdriver.Chrome()
        else:
            driver=webdriver.Edge()
        driver.get(url)
        driver.maximize_window()
        return driver

    def send_user_info(self,key,data):
        self.get_user_element(key).send_keys(data)

    def get_user_element(self,key):
        find_element=FindElement(self.driver)
        user_element=find_element.get_element(key)
        return user_element

    def get_range_user(self):
        user_info = ''.join(random.sample('1234567890abcdefg', 8))
        return user_info

    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        code_elem = self.get_user_element("code_image")
        print(code_elem.location)
        left = code_elem.location['x']
        top = code_elem.location['y']
        right = code_elem.size['width'] + left
        height = code_elem.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)

    def code_online(self,file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-4", "142568", "ba6ac2df392d4f259d35c3ee7bce20d2")
        r.addFilePara("image", file_name)
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addBodyPara("needMorePrecise", "0")
        res = r.post()
        text = res.json()["showapi_res_body"]["Result"]
        return text
    def main(self):
        user_name_info = self.get_range_user()
        user_email = user_name_info + '@163.com'
        file_name = "E:/image1.png"
        code_text=self.code_online(file_name)
        self.send_user_info('user_email',user_email)
        self.send_user_info('user_name', user_name_info)
        self.send_user_info('password', "111111")
        self.send_user_info('code_text', code_text)
        self.get_user_element("register_button").click()
        code_error=self.get_user_element("code-error")
        if code_error==None:
            print("注册成功")
        else:
            self.driver.save_screenshot("E:/error.png")
        time.sleep(25)
        self.driver.close()

if __name__ == '__main__':
    for i in range(3):
        r=RegisterFunction("http://www.5itest.cn/register",i)
        r.main()