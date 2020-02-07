from collections import OrderedDict

f = open("res.txt", 'r')
d = []
i = 0
names  = set()
for line in f.readlines():
	i +=1
	name =line.split("id:")[0].split(":")[-1].strip()
	if not name in names:
		cal_den = float(line.split()[0].strip(':'))
		d.append((cal_den,name))
		names.add(name)

i = 0
d.sort(key=lambda x: x[0], reverse=True)

out = open("rankings.txt", "w")
out.write("# Rank, Caloric density, Food Name\n")
for k,v in d:
	i+=1
	out.write("%d, %.5f, %s\n"%(i, k, v))
out.close()
