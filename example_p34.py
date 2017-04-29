#coding: utf-8

import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from pandas.tools.plotting import autocorrelation_plot

data = pd.read_table('data/ch2data/m-dec12910.txt', sep = '\s+', index_col = 0, parse_dates=True)

# pandas计算的自相关系数与R不一致
# print data.dec10.autocorr(lag=0)
# print data.dec10.autocorr(lag=1) # R: 0.227386585
# print data.dec10.autocorr(lag=12) # R: 0.130411045

print 'pandas: %s, R: %s'%(data.dec10.autocorr(lag=1), 0.227386585)
print 'pandas: %s, R: %s'%(data.dec10.autocorr(lag=12), 0.130411045)
