#coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_table('../data/ch3data/w-petroprice.txt', sep='\s+', header=0)
data1 = pd.read_table('../data/ch3data/w-gasoline.txt', sep='\s+', squeeze=True)

plt.subplot(211)
data.US.plot(title='Grude oil')

plt.subplot(212)
data1.plot(title='Gasoline')

plt.show()
