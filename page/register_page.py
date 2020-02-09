from base.find_element import FindElement
class RegisterPage(object):
    def __init__(self,driver):
        self.fd=FindElement(driver)
    def get_email_element(self):
        return self.fd.get_element("user_email")
    def get_username_element(self):
        return self.fd.get_element("user_name")
    def get_password_element(self):
        return self.fd.get_element("password")
    def get_code_element(self):
        return self.fd.get_element("code_text")
    def get_button_element(self):
        return self.fd.get_element("register_button")
    def get_email_error_element(self):
        return self.fd.get_element("user_email_error")
    def get_username_error_element(self):
        return self.fd.get_element("user_name_error")
    def get_password_error_element(self):
        return self.fd.get_element("password_error")
    def get_code_error_element(self):
        return self.fd.get_element("code-error")