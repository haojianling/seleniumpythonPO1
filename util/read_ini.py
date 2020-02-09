import configparser
class ReadIni(object):
    def __init__(self,file_name=None,node=None):
        if file_name==None:
            file_name="F:/workspace/python/py/config/LocalElement.ini"
        if node==None:
            self.node='registerElement'
        else:
            self.node=node
        self.cf=self.load_ini(file_name)
        print(self.cf)
    def load_ini(self,file_name):
        cf=configparser.ConfigParser()
        cf.read(file_name)
        return cf

    def get_vaule(self,key):
        data=self.cf.get(self.node,key)

        return data

if __name__ == '__main__':
    r=ReadIni()

    print(r.get_vaule('user_email'))