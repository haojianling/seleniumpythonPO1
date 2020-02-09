from PIL import Image
from ShowapiRequest import ShowapiRequest
import time
class GetCode(object):
    def __init__(self,driver):
        self.driver=driver
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        code_elem =self.driver.find_element_by_id("getcode_num")
        print(code_elem.location)
        left = code_elem.location['x']
        top = code_elem.location['y']
        right = code_elem.size['width'] + left
        height = code_elem.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)
        time.sleep(1)

    def code_online(self,file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-4", "142568", "ba6ac2df392d4f259d35c3ee7bce20d2")
        r.addFilePara("image", file_name)
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addBodyPara("needMorePrecise", "0")
        res = r.post()
        text = res.json()["showapi_res_body"]["Result"]
        time.sleep(2)
        return text