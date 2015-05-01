import numpy as np
import csv
import pandas
from six.moves import zip
import time
from numpy import cumprod, linspace, random
from bokeh.plotting import *
import bokeh.plotting as bp
from bokeh.models import HoverTool, ColumnDataSource
from collections import OrderedDict

df= pandas.DataFrame.from_csv('/home/pinar/DataSci15-MIT/Graphs/HOTS_bydepth1.csv')
bp.output_file('test.html')
df1 = df[df.depth == 0]
df2 = df[df.depth == 2]
df3 = df[df.depth == 4]
df4 = df[df.depth == 6]
df5 = df[df.depth == 8]
df6 = df[df.depth == 10]
df7 = df[df.depth == 12]
df8 = df[df.depth == 14]
df9 = df[df.depth == 16]
df10 = df[df.depth == 18]
df11 = df[df.depth == 20]

fig = bp.figure(tools="reset,hover")
temperature1 = df1.Temp
flour1=df1.Flour
temperature2 = df2.Temp
flour2=df2.Flour
temperature3 = df3.Temp
flour3=df3.Flour
temperature4 = df4.Temp
flour4=df4.Flour
temperature5 = df5.Temp
flour5=df5.Flour
temperature6 = df6.Temp
flour6=df6.Flour
temperature7 = df7.Temp
flour7=df7.Flour
temperature8 = df8.Temp
flour8=df8.Flour
temperature9 = df9.Temp
flour9=df9.Flour
temperature10 = df10.Temp
flour10=df10.Flour
temperature11 = df11.Temp
flour11=df11.Flour

# r.line(temperature1, flour1, color='#1F78B4', legend='ACME')
# r.line(temperature2, flour2, color='#FB9A99', legend='CHOAM')
# bp.show(r)

s1 = fig.scatter(x=temperature1,y=flour1,color='#0000ff',size=10,legend='0m')
s2 = fig.scatter(x=temperature2,y=flour2,color='#ff0000',size=10,legend='2m')
s3 = fig.scatter(x=temperature3,y=flour3,color='#b364d7', size=10,legend='4m')
# s4 = fig.scatter(x=temperature4,y=flour4,color='#00ff00',size=10,legend='6m')
# s5 = fig.scatter(x=temperature5,y=flour5,color='#3b73fc',size=10,legend='8m')
# s6 = fig.scatter(x=temperature6,y=flour6,color='#fe3562',size=10,legend='10m')
# s7 = fig.scatter(x=temperature7,y=flour7,color='#132030',size=10,legend='12m')
# s8 = fig.scatter(x=temperature8,y=flour8,color='#ba9bfa',size=10,legend='14m')
# s9 = fig.scatter(x=temperature9,y=flour9,color='#800080',size=10,legend='16m')
# s10 = fig.scatter(x=temperature10,y=flour10,color='#860506',size=10,legend='18m')
# s11= fig.scatter(x=temperature11,y=flour11,color='#2f8e20',size=10,legend='20m')

show(s1)