#coding:utf-8

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import util

data = pd.read_table('data/1/d-mmm-0111.txt', sep = '\s+', index_col=0)
MMMStats = util.basicStats(data.rtn)
print(MMMStats)
print(stats.ttest_1samp(data.rtn, 0))
plt.subplot(121)
plt.plot(data)
plt.subplot(122)
pdf, bins, patches = plt.hist(data.rtn.values, bins=1000)
x = np.arange(MMMStats['min'], MMMStats['max'], 0.001)
y = stats.norm.pdf(x, MMMStats['mean'], MMMStats['std'])
plt.plot(x, y)
plt.show()
