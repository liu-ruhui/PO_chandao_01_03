import os
import xlrd
from common.conf_utils import conf


current_path = os.path.dirname(__name__)
excel_path = os.path.join(current_path,'..//element_info_datas/element_infos.xlsx')

workbook = xlrd.open_workbook(excel_path)
sheet = workbook.sheet_by_name('项目')
row_count = sheet.nrows
col_count = sheet.ncols

element_infos = locals()
for i in range(1,row_count):
    element_info = {}
    for j in range(1,col_count):
        cell_value = sheet.cell_value(i, j)
        cell_value = int(cell_value) if isinstance(cell_value, float)else str(cell_value)
        # 将字符串模式的时间数字转化为整型
        element_info[sheet.cell_value(0, j)] = cell_value
    if element_info['page'] == 'login_page':
        element_infos[sheet.cell_value(i,0)] = {}
        element_infos[sheet.cell_value(i,0)] = element_info

try:
   print(element_infos['password_inputbox'])
except Exception as e:
    print('该页面无此参数')
# print(element_infos['username_inputbox'])
