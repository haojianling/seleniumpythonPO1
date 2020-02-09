from util.read_ini import ReadIni
class FindElement(object):
    def __init__(self,driver):
        self.driver=driver
    def get_element(self,key):
        read_ini=ReadIni()
        data=read_ini.get_vaule(key)
        by=data.split(">")[0]
        value=data.split('>')[1]
        try:
            if by=='id':
                return self.driver.find_element_by_id(value)
            elif by=='name':
                return self.driver.find_element_by_name(value)
            elif by=='className':
                return self.driver.find_element_by_class_name(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            self.driver.save_screenshot("E:/%s.png"%value)
            return None
