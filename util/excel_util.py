import xlrd
from xlutils.copy import copy
class ExcelUtil:
    def __init__(self,excel_path=None,index=None):
        if excel_path==None:
            self.excel_path="F:\workspace\python\py\config\datacase.xls"
        else:
            self.excel_path=excel_path
        if index==None:
            index=0
        self.data=xlrd.open_workbook(self.excel_path)
        self.table=self.data.sheets()[index]

    def get_data(self):
        result=[]
        rows=self.get_lines()
        if rows!=None:
            for i in range(rows):
                col=self.table.row_values(i)
                print(col)
                result.append(col)
            return result
        return None
    def get_lines(self):
        rows = self.table.nrows
        #判断行数
        if rows>=1:
            return rows
        return None

    def get_col_value(self,row,col):
        if self.get_lines()>row:
            data=self.table.cell(row,col).value
            return data
        return None


    #写入数据
    def wirte_value(self,row,value):
        read_value=xlrd.open_workbook(self.excel_path)
        write_data=copy(read_value)
        write_data.get_sheet(0).write(row,9,value)
        write_data.save(self.excel_path)
if __name__ == '__main__':
    ex=ExcelUtil("F:\workspace\python\py\config\keyword.xls")
    # print(ex.get_col_value())
    print(ex.wirte_value(7,"test"))