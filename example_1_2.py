#coding:utf-8

import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import util

data = pd.read_table('data/1/d-mmm-0111.txt', sep = '\s+', index_col=0)
print(util.basicStats(data.rtn))
print(stats.ttest_1samp(data.rtn, 0))
plt.plot(data.rtn, stats.norm.pdf(data.rtn))
plt.show()
