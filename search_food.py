#!/usr/bin/env python3
'''-------------------------------------
foo.py
backpacking

	by Daniel Richards (github.com/dan-rds)
	Copyright © 2019 Daniel Richards. All rights reserved.
-------------------------------------- 
'''

from usda.client import UsdaClient
from food import Food
import os
import os.path
output_filename = "res.txt"
db_index = 0
if os.path.isfile(output_filename):
	output = open(output_filename, 'r+')
	lines = output.readlines()
	db_index = int(lines[-1].split(' ')[-1])
	output.close()
	
else:
    print ("File not exist")
output = open("result.txt", 'a+')

client = MyClient("<your api key>") 
food_list = []

for offset in range(db_index,1000000, 500):
	foods = client.list_foods(500, offset=offset)
	ids = list([f.id for f in foods])

	for n in range(0,500, 25):
		food_list  = client.get_food_report_v2_raw(ndbno=ids[n:n+25])
		for i, f in enumerate(food_list['foods']):
			food_obj = Food(f)
			output.write("%0.5f: %s, id: %d\tDatabase index: %d\n"% (float(food_obj), str(food_obj), int(ids[n+i]), offset+n+i))
	output.flush()
	os.fsync(output.fileno())

output.close()

