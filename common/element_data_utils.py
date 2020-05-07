import os
import xlrd
from common.conf_utils import conf

current_path = os.path.dirname(__name__)
excel_path = os.path.join(current_path,'..//elemnt_info_datas/element_infos.xlsx')
class ElementDataUtils:
    def __init__(self,moudle_name,element_path = excel_path):
        self.element_path = element_path
        self.workbook = xlrd.open_workbook(element_path)  #打开存放的excel数据
        self.sheet = self.workbook.sheet_by_name(moudle_name) #按名称获取sheet
        self.row_count = self.sheet.nrows  #获取所有的行
        self.col_count = self.sheet.ncols  #获取所有的列
    def get_element_info(self, page_name):
            element_infos = locals()  # 动态获取数据
            for i in range(1, self.row_count):
                element_info = {}
                for j in range(1, self.col_count):
                    element_info[self.sheet.cell_value(0, j)] = self.sheet.cell_value(i, j)
                    timeout_value = self.sheet.cell_value(i, 4)
                    element_info['timeout'] = timeout_value if isinstance(timeout_value, float)else conf.time_out
                if element_info['page'] == page_name:
                    element_infos[self.sheet.cell_value(i, 0)] = {}
                    element_infos[self.sheet.cell_value(i, 0)] = element_info
            return element_infos



if __name__ =="__main__":
    # try:
        elemenets = ElementDataUtils('项目').get_element_info('login_page')
        print(elemenets['username_inputbox'])
    # except Exception as e:
    #     print('该页面无此参数')
#     #     for e in elemenets.values():
#     #         print(e)
