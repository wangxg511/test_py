from tqdm import tqdm
import re

# with open("over_time_log.txt", 'w', encoding='utf8') as f:
#     for line in tqdm(open('sc-info-20210410.0_184.log', encoding='utf8')):
#         res_list = re.findall(r'"timestamp":(.*?),',line)
#         if res_list:
#             if int(res_list[0]) < 1617984000000 or int(res_list[0]) >= 1618070400000:
#                 f.write(line)
#     with open('have186.txt',"w",encoding='utf8') as f1:
#         for line in tqdm(open('sc-info-20210410.0_186.log', encoding='utf8')):
#             res_list = re.findall(r'"timestamp":(.*?),',line)
#             if res_list:
#                 # print(res_list[0])
#                 f1.write(res_list[0]+',')
#                 if int(res_list[0]) < 1617984000000 or int(res_list[0]) >= 1618070400000:
#                     f.write(line)
#     for line in tqdm(open('sc-info-20210410.0_186.log', encoding='utf8')):
#         res_list = re.findall(r'"timestamp":(.*?),',line)
#         if res_list:
#             if int(res_list[0]) < 1617984000000 or int(res_list[0]) >= 1618070400000:
#                 f.write(line)

# print(re.findall(r'我们|名字', '我们的名字'))
str_dict={}
str_dict.has_key('222')