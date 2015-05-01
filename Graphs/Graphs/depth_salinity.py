import numpy as np
import csv
import pandas
from six.moves import zip
from bokeh.plotting import *
from bokeh.models import HoverTool, ColumnDataSource
from collections import OrderedDict
df1= pandas.DataFrame.from_csv('/home/pinar/DataSci15-MIT/Graphs/HOTS1.csv')
depth = df1.depth
temp = df1.Temp
salinity= df1.sal
oxygen=df1.oxy
chloropig=df1.fluor
TOOLS="resize,hover, save, crosshair,pan,wheel_zoom,box_zoom,reset,tap,previewsave,box_select,poly_select,lasso_select"
output_file("HOTS_depth_vs_salinity.html", title="HOTS_depth_vs_salinity")
p = figure(tools=TOOLS,title = 'HOTS C#1 Depth vs Salinity', x_axis_label="Depth",y_axis_label = "Salinity")
p.scatter(depth,salinity, radius=3, fill_color="#FA5858", fill_alpha=0.6, line_color=None)
p.xaxis.axis_label = "Depth (m)"
p.yaxis.axis_label = "Salinity (PSS-78)"
source = ColumnDataSource(
    data=dict(
        x=depth,
        y=salinity,
        depth = depth
      
    )
)
p.plot_width = 600
p.plot_height = 600
# p.rect('x', 'y', 0.9, 0.9, source=source,line_color=None)
hover = p.select(dict(type=HoverTool))
hover.tooltips = OrderedDict([
    ('Depth', '@x'),
    ('Salinity', '@y'),('Depth', '@depth')
])
show(p)  # open a browser