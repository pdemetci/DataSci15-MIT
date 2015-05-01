import numpy as np
import bokeh.plotting as bp
bp.output_file('test.html')

fig = bp.figure(tools="reset")
x = np.linspace(0,2*np.pi)
y1 = np.sin(x)
y2 = np.cos(x)
s1 = fig.scatter(x=x,y=y1,color='#0000ff',size=10,legend='sine')

s2 = fig.scatter(x=x,y=y2,color='#ff0000',size=10,legend='cosine')

bp.show(s1)