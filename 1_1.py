import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def basicStats(data):
    basicStats = pd.Series({
        'mean': data.mean(),
        'std': data.std(),
        'skew': data.skew(),
        'kurt': data.kurt(),
        'max': data.max(),
        'min': data.min()
    }, name=data.name)
    return basicStats

data = pd.read_table('data/1/d-axp3dx-0111.txt', sep='\s+', index_col=0)
print(basicStats(data.axp))
print(basicStats(np.log(1 + data.axp)))
#data.axp.plot()
#plt.show()
