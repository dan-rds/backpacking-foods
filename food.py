
from pprint import pprint
class Food(object):
	"""docstring for Food"""
	def __init__(self, food_dict):
		super(Food, self).__init__()

		temp_name = food_dict['food']['desc']['name'].lower()
		if 'upc:' in temp_name:
			temp_name= temp_name.split(', upc:')[0]
		if 'gtin:' in temp_name:
			temp_name= temp_name.split(', gtin:')[0]

		self.name = temp_name.title()
		try:
			self.kcal = int(food_dict['food']['nutrients'][0]['value'])
			self.equiv_amount = int(food_dict['food']['nutrients'][0]['measures'][0]['eqv'])
			self.equiv_unit = food_dict['food']['nutrients'][0]['measures'][0]['eunit']
		except IndexError:
			pprint("index error in Food")
			self.kcal = 0
			self.equiv_amount = 0
			self.equiv_unit = 'mg'
		except:
			self.kcal = 0
			self.equiv_amount = 0
			self.equiv_unit = 'mg'


		
		density = 0
		if self.equiv_amount:
			if self.equiv_unit == 'g':
				self.equiv_amount *= 1000
				self.equiv_unit = 'mg'

			density = self.kcal / self.equiv_amount

		self.kcals_per_mg = density
	def print(self):
		pprint(vars(self))
	def __float__(self):
		return float(self.kcals_per_mg)
	def __str__(self):
		return self.name