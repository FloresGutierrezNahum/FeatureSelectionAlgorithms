#https://pythonfordatascienceorg.wordpress.com/wilcoxon-sign-ranked-test-python/

import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv("blood_pressure.csv")

df[['bp_before','bp_after']].describe()

stats.probplot(df['bp_before'], dist="norm", plot=plt)
plt.title("Blood Pressure Before Q-Q Plot")
plt.savefig("BP_Before_QQ.png")

stats.probplot(df['bp_after'], dist="norm", plot=plt)
plt.title("Blood Pressure After Q-Q Plot")
plt.savefig("BP_After_QQ.png")

print(stats.shapiro(df['bp_before']))
print(stats.shapiro(df['bp_after']))
print(stats.wilcoxon(df['bp_before'], df['bp_after']))