# Function to detect NGE v from 
def nge_fct(shop_floors, r, y1, y2):
	for v in range(r+1, len(shop_floors), 1): 
		
		while y1+y2 != 2:
			if y1+y2 != 2:
				v += 1
				continue
			else:
				return [True, v]

