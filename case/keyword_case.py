from util.excel_util import ExcelUtil
from keywordselenium.actionMethod import ActionMethod
import sys
sys.path.append("F:\workspace\python\py")
class KeywordCase:
    def run_main(self):
        self.action_method = ActionMethod()
        handle_excel=ExcelUtil("F:\workspace\python\py\config\keyword.xls")
        #是否执行
        case_lines=handle_excel.get_lines()
        if case_lines:
            for i in range(1,case_lines):
                is_run=handle_excel.get_col_value(i,3)
                print(is_run)
                if is_run=='yes':
                    method=handle_excel.get_col_value(i, 4)
                    # print('meth====',method)
                    send_value=handle_excel.get_col_value(i, 5)
                    handle_value=handle_excel.get_col_value(i, 6)
                    except_result_method=handle_excel.get_col_value(i,7)
                    except_result = handle_excel.get_col_value(i, 8)
                    self.run_method(method,send_value,handle_value)
                    if except_result!='':
                        except_value=self.get_except_result_value(except_result)
                        if except_value[0]=='text':
                            result=self.run_method(except_result_method)
                            # print('result>>>>>>>',result)
                            # print(except_value[1])
                            if except_value[1] in result:
                                handle_excel.wirte_value(i,'pass')
                            else:
                                handle_excel.wirte_value(i,'fail')
                        elif except_value[0]=='element':
                            print('except_value=====',except_value[1])
                            result=self.run_method(except_result_method,except_value[1])
                            print('result====',result)
                            if result:
                                handle_excel.wirte_value(i,'pass')
                            else:
                                handle_excel.wirte_value(i,'fail')


    def get_except_result_value(self,data):
        return data.split('=')


    def run_method(self,method,send_value='',handle_value=''):
        method_value=getattr(self.action_method, method)
        if send_value=='' and handle_value!='':
            # print("=========",handle_value,send_value)
            result=method_value(handle_value)
        elif send_value!='' and handle_value!='':
            result=method_value(send_value,handle_value)
        elif send_value != '' and handle_value == '':
            result=method_value(send_value)
        else:
            result=method_value()
        return result


if __name__ == '__main__':
    KeywordCase().run_main()