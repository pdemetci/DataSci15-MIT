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
output_file("HOTS_temp_vs_salinity.html", title="HOTS_temp_vs_salinity")
p = figure(tools=TOOLS,title = 'HOTS C#1 Temp vs Salinity', x_axis_label="Temp",y_axis_label = "Salinity")
p.scatter(temp,salinity, radius=0.2, fill_color="#04B404", fill_alpha=0.6, line_color=None)
p.xaxis.axis_label = "Temperature (Celcius)"
p.yaxis.axis_label = "Salinity (PSS-78)"
source = ColumnDataSource(
    data=dict(
        x=temp,
        y=salinity,
      
    )
)
p.plot_width = 600
p.plot_height = 600
# p.rect('x', 'y', 0.9, 0.9, source=source,line_color=None)
hover = p.select(dict(type=HoverTool))
hover.tooltips = OrderedDict([
    ('Temperature', '@x'),
    ('Salinity', '@y'),
])
show(p)  # open a browser