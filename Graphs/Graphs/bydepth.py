import numpy as np
import csv
import pandas
from six.moves import zip
from bokeh.plotting import *
from bokeh.models import HoverTool, ColumnDataSource
from collections import OrderedDict
df= pandas.DataFrame.from_csv('/home/pinar/DataSci15-MIT/Graphs/HOTS_bydepth1.csv')
# df1 = df[df.press == 0]
# df2 = df[df.press == 2]
# df3 = df[df.press == 4]
# df4 = df[df.press == 6]
# df5 = df[df.press == 8]
# df6 = df[df.press == 10]
# df7 = df[df.press == 12]
# df8 = df[df.press == 14]
# df9 = df[df.press == 16]
# df10 = df[df.press == 18]
# df11 = df[df.press == 20]


# temperature1 = df1.Temp
# flour1=df1.Flour
# temperature2 = df2.Temp
# flour2=df2.Flour
# temperature3 = df3.Temp
# flour3=df3.Flour
# temperature4 = df4.Temp
# flour4=df4.Flour
# temperature5 = df5.Temp
# flour5=df5.Flour
# temperature6 = df6.Temp
# flour6=df6.Flour
# temperature7 = df7.Temp
# flour7=df7.Flour
# temperature8 = df8.Temp
# flour8=df8.Flour
# temperature9 = df9.Temp
# flour9=df9.Flour
# temperature10 = df10.Temp
# flour10=df10.Flour
# temperature11 = df11.Temp
# flour11=df11.Flour

temp = df.Temp
depth = df.depth
#salinity= df1.sal
#oxygen=df1.oxy
chloropig=df.Flour

print temp
print chloropig
TOOLS="resize,hover, save, crosshair,pan,wheel_zoom,box_zoom,reset,tap,previewsave,box_select,poly_select,lasso_select"
output_file("HOTS_temp_vs_salinity.html", title="HOTS_temp_vs_salinity")
p = figure(tools=TOOLS,title = 'HOTS C#1 Temp vs Salinity', x_axis_label="Temp",y_axis_label = "Salinity")
# if depth ==0 :
# 	a="#800080"
# if depth ==2 :
# 	a= "#67c8ff"
# else:
# 	a= "#00ff00"
# if depth ==4 :
# 	a=
# if depth ==6 :
# 	a=
# if depth ==8 :
# 	a=
# if depth ==10 :
# 	a=
# if depth ==12 :
# 	a=
# if depth ==14 :
# 	a=
# if depth ==16 :
# 	a=
# if depth ==18 :
# 	a=
# if depth ==20 :
# 	a=


p.scatter(depth,chloropig, radius=0.1, fill_color="#800080", fill_alpha=0.6, line_color=None)
p.xaxis.axis_label = "Temperature (Celcius)"
p.yaxis.axis_label = "Salinity (PSS-78)"
# source = ColumnDataSource(
#     data=dict(
#         x=temp,
#         y=chloropig,
      
#     )
# )
p.plot_width = 600
p.plot_height = 600
# p.rect('x', 'y', 0.9, 0.9, source=source,line_color=None)
# hover = p.select(dict(type=HoverTool))
# hover.tooltips = OrderedDict([
#     ('Temperature', '@x'),
#     ('Salinity', '@y'),
# ])
show(p)  # open a browser

# #xyvalues = pd.DataFrame(xyvalues)
# #xyvalues = xyvalues.values()
# xyvalues = np.array(df.values())
# output_file("HOTS_temp_vs_chloropigment.html", title="HOTS_temp_vs_chloropigment")

# chart = Line(xyvalues, title="HOTS Depth 0-20m Temperature vs Chloropigment", ylabel='Temperature', legend=True)

# show(chart)

# p.xaxis.axis_label = "Temperature (Celcius)"
# p.yaxis.axis_label = "Chloropigment (ug/kg)"
# source = ColumnDataSource(
#     data=dict(
#         x=temp,
#         y=Chloropigment,
      
#     )
# )
# p.plot_width = 600
# p.plot_height = 600
# # p.rect('x', 'y', 0.9, 0.9, source=source,line_color=None)
# hover = p.select(dict(type=HoverTool))
# hover.tooltips = OrderedDict([
#     ('Temperature', '@x'),
#     ('Salinity', '@y'),
# ])
# show(p)  # open a browser