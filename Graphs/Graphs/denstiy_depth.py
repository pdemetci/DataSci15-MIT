import numpy as np
import csv
import pandas
from six.moves import zip
from bokeh.plotting import *
from bokeh.models import HoverTool, ColumnDataSource
from collections import OrderedDict
df1= pandas.DataFrame.from_csv('/home/pinar/DataSci15-MIT/Graphs/HOTS1.csv')
depth = df1.depth
depth_mean = df1.depth.Mean()
temp = df1.Temp
temp_mean = df1.temp.Mean()
density=df1.theta
density_mean = df1.theta.Mean()
salinity= df1.sal
salinity_mean = df1.sal.Mean()
oxygen=df1.oxy
oxygen_mean = df1.oxy.Mean()
chloropig=df1.fluor
chloropig_mean = df1.fluor.Mean()
print depth_mean
print temp_mean
print density_mean
print salinity_mean
print oxygen_mean
print chloropig_mean

TOOLS="resize,hover, save, crosshair,pan,wheel_zoom,box_zoom,reset,tap,previewsave,box_select,poly_select,lasso_select"
output_file("HOTS_depth_vs_salinity.html", title="HOTS_depth_vs_salinity")
p = figure(tools=TOOLS,title = 'HOTS C#1 Density vs Depth', x_axis_label="Depth",y_axis_label = "Salinity")
p.scatter(depth,density, radius=3, fill_color="#FA5858", fill_alpha=0.6, line_color=None)
p.xaxis.axis_label = "Depth (m)"
p.yaxis.axis_label = "Density of Bacteria Samples (kg/m3)"
source = ColumnDataSource(
    data=dict(
        x=depth,
        y=density,      
    )
)
p.plot_width = 600
p.plot_height = 600
# p.rect('x', 'y', 0.9, 0.9, source=source,line_color=None)
hover = p.select(dict(type=HoverTool))
hover.tooltips = OrderedDict([
    ('Depth', '@x'),
    ('Density', '@y'),('Depth', '@depth')
])
show(p)  # open a browser