import numpy as np
import csv
import pandas
import statsmodels.formula.api as smf
import thinkplot 
df1= pandas.DataFrame.from_csv('/home/pinar/DataSci15-MIT/Graphs/HOTS1.csv')
depth = df1.depth
temp = df1.Temp
salinity= df1.sal
oxygen=df1.oxy
fluor=df1.fluor
formula = 'fluor ~ depth'
model = smf.ols(formula,data=df1)
results=model.fit()
results= thinkplot.Show()