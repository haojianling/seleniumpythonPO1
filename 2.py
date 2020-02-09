import pytesseract
from PIL import Image
from ShowapiRequest1 import ShowapiRequest
# image=Image.open("E:/impoc1.png")
# text=pytesseract.image_to_string(image)
# print(text)
#https://www.showapi.com/api/apiList   验证码
r = ShowapiRequest("http://route.showapi.com/184-4", "142568", "ba6ac2df392d4f259d35c3ee7bce20d2" )
r.addFilePara("image", r"E:/impoc1.png")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
res = r.post()
text=res.json()["showapi_res_body"]["Result"]
print(text)



