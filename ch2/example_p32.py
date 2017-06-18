# coding: utf-8

import pandas as pd

data = pd.read_table('data/ch2data/m-ibmsp6709.txt', sep = '\s+', index_col = 0)

# sp与ibm的相关系数
print data.sp.corr(data.ibm)
print data.sp.corr(data.ibm, method='spearman')
print data.sp.corr(data.ibm, method='kendall')
