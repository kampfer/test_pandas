#coding: utf-8

import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from pandas.tools.plotting import autocorrelation_plot

data = pd.read_table('data/ch2data/m-dec12910.txt', sep = '\s+', index_col = 0)
# plt.subplot(311)
# data.dec10.plot()
# plt.subplot(312)
# plt.plot(data.dec10)
# plt.subplot(313)
autocorrelation_plot(data.dec10)
plt.show()
