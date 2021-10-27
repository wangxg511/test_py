import pandas as pd

# dict_file_path = '对应表.xlsx'
# dict_file_path = '新建 Microsoft Excel 工作表.xlsx'
dict_file_path = '乡镇街道代码(公安).xls'
file_path = '行政区划映射数据.xlsx'


# 获取code：space字典
sheet = pd.read_excel(dict_file_path, keep_default_na=False)
list_ = []
code_dress_dict = {}
for line in sheet.values:
    # if int(line[3]) == 1:
    if True:
        code = int(line[0])
        space = line[1]
        if code != '':
            if code not in list_:
                code_dress_dict[code] = space
                list_.append(code)
            else:
                print(dict_file_path, '出现重复的乡镇街道代码为：', code)


sheet1 = pd.read_excel(file_path, keep_default_na=False)
code_list = []
code_list_h = set()
code_list_no = set()
for row in sheet1.values:
    code_list.append(row[1])
    if code_dress_dict.get(row[1]):
        code_list_h.add(row[1])
    else:
        code_list_no.add(row[1])
        print(row[1])

code_dict_key_no = set()
for key in code_dress_dict.keys():
    if key not in code_list:
        code_dict_key_no.add(key)

print("行政区域表在对应表中存在数目：", len(code_list_h))
print("行政区域表在对应表中不存在数目：", len(code_list_no))
print("对应表在行政区域表中存在数目：", len(code_dress_dict.keys()) - len(code_dict_key_no))
print("对应表在行政区域表中不存在数目：", len(code_dict_key_no))
