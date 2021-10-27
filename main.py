g_list = []
t_list = []
for line in open("gaoyy.txt","r",encoding='utf8'):
  if line.strip():
    if "T" in line:
      t_list.append(line.split(' '))
    if "G" in line:
      g_list.append(line.split(" "))

t_list.sort(key=lambda line:float(line[0]),reverse=True)
g_list.sort(key=lambda line:float(line[0]),reverse=True)

with open("g.txt",'w',encoding='utf8') as f:
  for i in g_list:
    f.write(str(i).replace('\\n','')+'\n')
with open("t.txt",'w',encoding='utf8') as f:
  for i in t_list:
    f.write(str(i).replace('\\n','')+'\n')