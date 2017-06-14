# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_table('../data/ch3data/w-petroprice.txt', sep='\s+', header=0)
data1 = pd.read_table('../data/ch3data/w-gasoline.txt', sep='\s+', squeeze=True)
lnPrice = np.log(data.US)
lnPrice1 = np.log(data1)

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

plt.acorr(priceReturn1, maxlags=30)
plt.show()
