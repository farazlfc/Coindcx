import math

import numpy as np
import pandas as pd

class Custom:
	@staticmethod
	def get_custom(data, width, back_test=False):
		if back_test == True:
			arr = data['close'].values
		else:
			arr = [a for a in reversed(data['close'])]
		df = pd.Series(arr)
		ma = df.rolling(w).mean()
		lower, upper = 80, 84




		return 	{"ma" : ma.values, "upper": upper, "lower": lower}