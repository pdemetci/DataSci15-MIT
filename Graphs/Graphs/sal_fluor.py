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
output_file("salinity_vs_chloropigment.html", title="salinity_vs_chloropigment")
p = figure(tools=TOOLS,title = 'HOTS C#1 Salinity vs Chloropigment', x_axis_label="Salinity",y_axis_label = "Chloropigment")
p.scatter(salinity,chloropig, radius=0.01, fill_color="#4B088A", fill_alpha=0.6, line_color=None)
p.xaxis.axis_label = "Salinity (PSS-78)"
p.yaxis.axis_label = "Chloropigment Concentration (ug/L)"
source = ColumnDataSource(
    data=dict(
        x=salinity,
        y=chloropig,
      
    )
)
p.plot_width = 600
p.plot_height = 600
# p.rect('x', 'y', 0.9, 0.9, source=source,line_color=None)
hover = p.select(dict(type=HoverTool))
hover.tooltips = OrderedDict([
    ('Salinity', '@x'),
    ('Chloropigment', '@y'),
])
show(p)  # open a browser