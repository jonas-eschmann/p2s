import numpy as np
from .flat import data
print(f"Mean: {np.nanmean(data)}\nStd: {np.nanstd(data)}")