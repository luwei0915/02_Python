import xlwt
import  datetime as dt   # 写入日期用

xls = xlwt.Workbook(encoding="utf-8")   # 创建一个xls对象,用来保存对excel表的操作
for i in range(1,6):                    # 写5个sheet页
    # 给 xls 添加一张‘成绩表’的表格
    sheet = xls.add_sheet('成绩表_' + str(i), cell_overwrite_ok=True)
    font = xlwt.Font()                  # 创建一个font对象，用来保存对字体进行的操作

    # 字体样式
    font.name = '微软雅黑'             # 将字体设置为'微软雅黑'
    font.bold = True                    # 设置字体加粗
    font.underline = True               # 设置字体加下划线
    font.italic = True                  # 设置字体倾斜

    # 背景样式
    pattern = xlwt.Pattern()            # 创建一个pattern对象，用来保存单元格背景的样式
    pattern.pattern = 0x02              # 设置单元格的背景图案样式（0x01-0x12共18种样式）
    pattern.pattern_fore_colour = xlwt.Style.colour_map['yellow']  # 设置单元格的背景颜色

    # 应用样式
    style = xlwt.XFStyle()              # 创建一个style对象，用来保存excel的样式
    style_date = xlwt.XFStyle()         # 写入日期用
    style.font = font                   # 将字体信息保存到style对象中
    style.pattern = pattern             # 将背景颜色信息保存到styke对象中
    style_date.num_format_str = 'yyyy/mm/dd' # 指定输出日期的格式

    # 列宽
    first_col = sheet.col(0)  # 获得测试表中横坐标为0的列
    first_col.width = 256 * 20  # 将或的的列的宽设置为256*20个单位，即20个10号字的0的宽度

    # 写入数据
    sheet.write(0, 0, '学生姓名')       # 在坐标为0,0的单元格内添加内容'学生姓名'
    sheet.write(0, 1, '成绩')           # 在坐标为1,1的单元格内添加内容'成绩'　　
    sheet.write(0, 2, '评语')           # 在坐标为0,2的单元格内添加内容'评语'
    sheet.write(1, 0, '张三',style)
    sheet.write(1, 1, 88,style)
    sheet.write(1, 2, '差得远',style)
    sheet.write(9, 0, dt.date.today(),style=style_date)   # 写入日期

    # 合并单元格操作 (纵坐标开始 纵坐标结束 横坐标开始 横坐标结束，数据，样式）
    # 将坐标为4,0和4,1的两列合并，并添加内容'合并两列'
    sheet.write_merge(4, 4, 0, 1, '合并两列',style)
    # 将坐标为2,0和3,0的两行合并，并添加内容'合并两行'
    sheet.write_merge(2, 3, 0, 0, '合并两行',style)
    # # 将纵坐标为5-7横坐标为0-2的三行三列合并，并添加内容'合并三行三列'
    sheet.write_merge(5, 7, 0, 2, '合并三行三列')

    # 插入公式
    sheet.write(8, 0, 1,style)
    sheet.write(8, 1, 1,style)
    sheet.write(8, 2, xlwt.Formula('A9+B9'),style)
xls.save('test.xls')                     # 将xls保存为'test'
'''
style_compression 表示是否压缩，不常用。
Workbook 还有一些属性：
Owner 设置文档所有者。
country_code： 国家码
wnd_protect： 窗口保护
obj_protect： 对象保护
Protect： 保护
backup_on_save： 保存时备份
Hpos： 横坐标
Vpos： 纵坐标
Width： 宽度
Height： 高度
active_sheet： 活动sheet
tab_width： tab宽度
wnd_visible： 窗口是否可见
wnd_mini： 窗口最小化
hscroll_visible： 横向滚动条是否可见。
vscroll_visible： 纵向滚动条是否可见。
tabs_visible： tab是否可见。
dates_1904： 是否使用1904日期系统
use_cell_values： 单元格的值
default_style： 默认样式
colour_RGB： 颜色

方法有：
add_style，add_font，add_str，del_str，str_index，add_rt，
rt_index，add_sheet，get_sheet，raise_bad_sheetname，convert_sheetindex，
setup_xcall，add_sheet_reference。
'''
