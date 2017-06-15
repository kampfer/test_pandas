# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

data = pd.read_table('../data/ch3data/w-petroprice.txt', sep='\s+', header=0)
data1 = pd.read_table('../data/ch3data/w-gasoline.txt', sep='\s+', squeeze=True)
lnPrice = np.log(data.US)
lnPrice1 = np.log(data1)
price1Return = data1.pct_change()

'''
plt.subplot(221)
ax = data.US.plot(title='Grude oil')
ax.set_ylabel('price')

plt.subplot(222)
ax = lnPrice.plot(title='Ln price of Grude oil')
ax.set_ylabel('ln price')

plt.subplot(223)
ax = data1.plot(title='Gasoline')
ax.set_ylabel('price')

plt.subplot(224)
ax = lnPrice1.plot(title='Ln price of gasoline')
ax.set_ylabel('ln price')

plt.show()

priceReturn1 = data1.pct_change()
priceReturn1.plot()

plt.show()
'''

f = plt.figure()
ax1 = f.add_subplot(211)
plot_acf(price1Return, lags=31, ax=ax1)
plt.show()
