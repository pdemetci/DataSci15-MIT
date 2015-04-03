import numpy as np
import csv
import pandas
from six.moves import zip
from bokeh.plotting import *
from bokeh.models import HoverTool, ColumnDataSource
from collections import OrderedDict
df1= pandas.DataFrame.from_csv('/home/pinar/Desktop/DATA/ALL_DATA/HOTS/HOT22csv')
x = df1.Temp
y = df1.Flour
# output to static HTML file
output_file("chloropigment.html", title="Chloropigment Concentration vs Temperature")

# create a new plot with a title and axis labels
TOOLS="resize,hover, save, crosshair,pan,wheel_zoom,box_zoom,reset,tap,previewsave,box_select,poly_select,lasso_select"
p = figure(tools=TOOLS, title="Chloropigment Concentration vs Temperature", x_axis_label='Temperature', y_axis_label='Chloropigment concentration')

# add a line renderer with legend and line thickness
source = ColumnDataSource(
    data=dict(
        x=x,
        y=y,
        
    )
)
p.plot_width = 600
p.plot_height = 600
hover = p.select(dict(type=HoverTool))
hover.tooltips = OrderedDict([
    ('Temperature', '@x'),
    ('concentration', '@y'),
])
p.line(x, y, legend="Temp.", line_width=2)
# show the results
show(p)