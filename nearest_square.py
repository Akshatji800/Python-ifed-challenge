from math import sqrt
from math import floor
def nearest_square(n):
	if n<0:
		return 0
	else:
		return floor(sqrt(n))**2
