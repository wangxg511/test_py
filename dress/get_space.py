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
data_list = []
head_list = list(sheet1.head(0))
for row in sheet1.values:
    code_list.append(row[1])
    if code_dress_dict.get(row[1]):
        row[2] = code_dress_dict.get(row[1])
        code_list_h.add(row[1])
    else:
        code_list_no.add(row[1])
    # print(len(row))
    dict_tmp = dict(zip(head_list,row))
    data_list.append(dict_tmp)

df = pd.DataFrame(data_list)
df.to_excel('./行政区划映射数据(有街道名称).xlsx',header=True,index=False)



f_path = '行政区划映射数据(有街道名称).xlsx'

f_path_sr = '乡镇街道区划(思锐).xlsx'

sr_list = pd.read_excel(f_path_sr,keep_default_na=False).values

sheet2 = pd.read_excel(f_path,keep_default_na=False)
data_sr_list = []
for row in sheet2.values:
    if row[2].strip() != '本级':
        for line1 in sr_list:
            # print(str(line1[0])[:-2])
            # print(row[2].strip())
            # print(line1[2].strip())
            if str(row[5]) == str(line1[0])[:-2] and row[2].strip() == line1[2].strip():
                row[7] = line1[0]
                row[8] = line1[2].strip()
                # print(1)

    data_sr_list.append(dict(zip(head_list,row)))



df = pd.DataFrame(data_sr_list)
df.to_excel('./行政区划映射数据(公安-思锐).xlsx',header=True,index=False)


code_dict_key_no = set()
for key in code_dress_dict.keys():
    if key not in code_list:
        code_dict_key_no.add(key)

print("行政区域表在对应表中存在数目：", len(code_list_h))
print("行政区域表在对应表中不存在数目：", len(code_list_no))
print("对应表在行政区域表中存在数目：", len(code_dress_dict.keys()) - len(code_dict_key_no))
print("对应表在行政区域表中不存在数目：", len(code_dict_key_no))
