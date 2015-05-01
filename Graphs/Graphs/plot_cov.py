import numpy as np
import csv
import pandas
from math import *
import thinkstats2

def Cov(xs,ys,meanx=None, meany=None):
	xs=np.asarray(xs)
	ys=np.asarray(ys)
	if meanx is None:
		meanx=np.mean(xs)
	if meany is None:
		meany=np.mean(ys)

	cov=np.dot(xs-meanx, ys-meany)/len(xs)
	return cov

def Corr(xs,ys):
	xs=np.asarray(xs)
	ys=np.asarray(ys)
	meanx = Mean(xs)
	varx= Var(xs)
	meany = Mean(ys)
	vary=Var(ys)

	corr=Cov(xs,ys, meanx, meany)/ math.sqrt(varx * vary)
	return corr 


df1= pandas.DataFrame.from_csv('/home/pinar/Desktop/DATA/ALL_DATA/HOTS/HOTS31_1.csv')
xs = df1.Temp
ys = df1.Flour
print Corr(xs, ys)

