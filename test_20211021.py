import uuid
m = input("M种状态：")
p = input("每种状态的频率，空格隔开：")
n = input("传入状态序列个数：")
status_id = input("状态编码：")

m_list = []
for i in range(int(m)):
    m_list.append(uuid.uuid4())
p_list = p.split(" ")
dct = dict(zip(m_list, p_list))
sort_dct = {item: index+1 for index, item in enumerate(sorted(dct.keys(), key=lambda x: dct.get(x), reverse=True))}
bit_num = sum([sort_dct.get(m_list[int(item)]) for item in status_id.split(",")])
print(bit_num)
