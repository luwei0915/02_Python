import xlrd

#打开excel文件读取数据
exce = xlrd.open_workbook('./test.xls')

#获取excel中对应的sheet
print('所有sheet名称',exce.sheet_names()) #获取所有sheet名称
# 所有sheet名称 ['成绩表_1', '成绩表_2', '成绩表_3', '成绩表_4', '成绩表_5']

sheets = exce.sheets()                      #获取所有sheets
#sheet = exce.sheets()[0]                   #也可以通过下标去访问某个具体的sheet
sheet1 = exce.sheet_by_name('成绩表_2')    #通过sheet名称获取
#sheet2 = exce.sheet_by_index(1)            #通过下标获取某个sheet

#获取sheet中行数和列数
nrows = sheet1.nrows
ncols = sheet1.ncols
print('对应sheet中行数：%d行，列数：%d列'% (nrows,ncols))
# 对应sheet中行数：10行，列数：3列

#获取sheet中整行或整列的数据(数组)
row0 = sheet1.row_values(0)     #通过下标获取某一行的数据
col0 = sheet1.col_values(0)     #通过下标获取某一列的数据
print('某行的数据：',row0)
print('某列的数据：',col0)     # 行合并，则行内容为首行的内容，后续合并行为空

#获取sheet中某个单元格的数据
cell_A5 = sheet1.cell(5,0).value    #第6行第1列  行合并则为合并行的首行内容
cell_B2 = sheet1.cell(1,1).value    #第2行第2列
cell_A9 = sheet1.cell(9,0).value    #第10行第1列
print('第6行第0列：',cell_A5)      # 合并三行三列
print('第2行第1列：',cell_B2)      # 88.0
print('第10行第1列：',cell_A9)     # 43829.0   2019/12/30 日期类型

#获取单元格数据类型
A5_ctype = sheet1.cell(5,0).ctype   # str类型
B2_ctype = sheet1.cell(1,1).ctype   # 数字类型
A9_ctype = sheet1.cell(9,0).ctype   #data类型
print('str类型：',A5_ctype)
print('数字类型：',B2_ctype)
print('data类型：',A9_ctype)        # 日期类型 2019/12/30

# 处理日期格式
# print(xlrd.xldate_as_datetime(sheet1.cell(9,0).value,0))    #转换成日期格式
# print(xlrd.xldate_as_tuple(sheet1.cell(9,0).value,0))       #返回元组
# 2019-12-30 00:00:00
# (2019, 12, 30, 0, 0, 0)


#写成函数处理，如果ctype等于3，就用时间格式处理
def xldate_datetime(sheet,row,col):
    if(sheet.cell(row,col).ctype==3):
        # 返回日期格式
        date_value_datetime = xlrd.xldate_as_datetime(sheet.cell(row,col).value,0)
        # date_value_tuple = xlrd.xldate_as_tuple(sheet.cell(row, col).value, 0)
        return date_value_datetime
print(xldate_datetime(sheet1,9,0))

print(sheet1.merged_cells) # 读取合并的单元格，但是读不出来
