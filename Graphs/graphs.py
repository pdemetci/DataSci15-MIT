import numpy as np
import csv
import pandas
from six.moves import zip
from bokeh.plotting import *
from bokeh.models import HoverTool, ColumnDataSource
from collections import OrderedDict
from bokeh.resources import CDN 
from bokeh.embed import file_html

numbers=[]
for i in range(1, 21):
	numbers.append(i)
for i in range(22,207):
	numbers.append(i)
for i in range(208, 218):
	numbers.append(i)
for i in range(219, 259):
	numbers.append(i)

df1= pandas.DataFrame.from_csv('/home/pinar/DataSci15-MIT/CleanedData/HOTS/HOTS.csv')

for i in numbers:
	df = df1[df1.crn == i]
	depth = df.press
	temp = df.temp
	TOOLS="resize,hover, save, crosshair,pan,wheel_zoom,box_zoom,reset,tap,previewsave,box_select,poly_select,lasso_select"
	output_file("depth_vs_temperature.html", title="depth_vs_temperature")
	name= 'HOTS C#' + str(i)+ ' Depth vs Temperature'
	p = figure(tools=TOOLS,title = name, x_axis_label="Depth",y_axis_label = "Temperature")
	p.scatter(depth,temp, radius=3, fill_color="#000000", fill_alpha=0.6, line_color=None)
	p.xaxis.axis_label = "Depth (m)"
	p.yaxis.axis_label = "Temperature (Celcius)"
	source = ColumnDataSource(
	    data=dict(
	        x=depth,
	        y=temp,
	      
	    )
	)
	p.plot_width = 600
	p.plot_height = 600
	# p.rect('x', 'y', 0.9, 0.9, source=source,line_color=None)
	hover = p.select(dict(type=HoverTool))
	hover.tooltips = OrderedDict([
	    ('Depth', '@x'),
	    ('Temperature', '@y'),
	])
	show(p)  # open a browser
	f = open(name+'.html', 'wb')
	html = file_html(p, CDN, name)
	f.write(html)
