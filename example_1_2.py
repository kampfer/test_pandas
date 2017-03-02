#coding:utf-8

import pandas as pd
import util

data = pd.read_table('data/1/d-mmm-0111.txt', sep = '\s+', index_col=0)
print(util.basicStats(data.rtn))
# print(util.basicStats2(data.rtn.values))
