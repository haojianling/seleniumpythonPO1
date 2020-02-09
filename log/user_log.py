import logging,os,datetime
class UserLog(object):
    def __init__(self):
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # consle=logging.StreamHandler()
        # logger.addHandler(consle)

        base_dir=os.path.dirname(os.path.abspath(__file__))
        log_dir=os.path.join(base_dir,"logs")
        log_file=datetime.datetime.now().strftime("%Y-%m-%d")+'.log'
        log_name=log_dir+"/"+log_file
        self.find_handle=logging.FileHandler(log_name,'a',encoding='utf-8')
        self.find_handle.setLevel(logging.INFO)
        fomatter=logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(lineno)d : %(levelname)s--------> %(message)s')
        self.find_handle.setFormatter(fomatter)
        self.logger.addHandler(self.find_handle)

        self.logger.debug("td都是ext")

    def get_logger(self):
        return self.logger

    def close_handle(self):
        self.find_handle.close()
        self.logger.removeHandler(self.find_handle)

if __name__ == '__main__':
    user=UserLog()
    log=user.get_logger()
    log.debug("tetetetetre")
    user.close_handle()
