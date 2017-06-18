#coding: utf-8

import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from pandas.tools.plotting import autocorrelation_plot

data = pd.read_table('data/ch2data/m-dec12910.txt', sep = '\s+', index_col = 0, parse_dates=True)

plt.subplot(311)
data.dec10.plot.line()

# pandas的自相关函数图
plt.subplot(312)
pd.tools.plotting.autocorrelation_plot(data.dec10)

# matplotlib的自相关函数图
plt.subplot(313)
plt.acorr(data.dec10, maxlags=24)

plt.show()

print data.dec10.autocorr(lag=1)
