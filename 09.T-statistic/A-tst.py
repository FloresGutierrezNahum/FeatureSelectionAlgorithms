#https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html

from scipy import stats
import numpy as np


rvs1 = stats.norm.rvs(loc=5,scale=10,size=500)
rvs2 = stats.norm.rvs(loc=5,scale=10,size=500)

print(stats.ttest_ind(rvs1,rvs2))
print(stats.ttest_ind(rvs1,rvs2, equal_var = False))

rvs3 = stats.norm.rvs(loc=5, scale=20, size=500)
print(stats.ttest_ind(rvs1, rvs3))

rvs5 = stats.norm.rvs(loc=8, scale=20, size=100)
stats.ttest_ind(rvs1, rvs5)

stats.ttest_ind(rvs1, rvs5, equal_var = False)

stats.ttest_ind(rvs1, rvs5)
stats.ttest_ind(rvs1, rvs5, equal_var = False)