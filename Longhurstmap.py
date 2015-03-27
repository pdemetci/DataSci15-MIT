import bokeh as bk
import shapefile 
import random
def getParts ( shapeObj ):

    points = []

    num_parts = len( shapeObj.parts )
    end = len( shapeObj.points ) - 1
    segments = list( shapeObj.parts ) + [ end ]


    for i in range( num_parts ):
        points.append( shapeObj.points[ segments[i]:segments[i+1] ] )


    return points

def getDict ( state_name, shapefile ):

    stateDict = {state_name: {} }

    rec = []
    shp = []
    points = []


    # Select only the records representing the
    # "state_name" and discard all other
    for i in shapefile.shapeRecords( ):

        if i.record[1] == state_name:
            rec.append(i.record)
            shp.append(i.shape)


    # In a multi record state for calculating total area
    # sum up the area of all the individual records
    #        - first record element represents area in cms^2
    #total_area = sum( [float(i[0]) for i in shp] ) / (1000*1000)


    # For each selected shape object get
    # list of points while considering the cases where there may be
    # multiple parts  in a single record
    for j in shp:
        for i in getParts(j):
            points.append(i)

    # Prepare the dictionary
    # Seperate the points into two separate lists of lists (easier for bokeh to consume)
    #      - one representing latitudes
    #      - second representing longitudes

    lat = []
    lng = []
    for i in points:
        lat.append( [j[0] for j in i] )
        lng.append( [j[1] for j in i] )


    stateDict[state_name]['lat_list'] = lat
    stateDict[state_name]['lng_list'] = lng
#    stateDict[state_name]['total_area'] = total_area

    return stateDict


dat = shapefile.Reader("/home/anna/Downloads/L-ocean/Longhurst_world_v4_2010.shp")

print dat.iterRecords

# Create a random dict of longhurst regions and colors
regions = set([i[1] for i in dat.iterRecords()])
print regions

rcolors = {}

for i in regions:
	r = lambda: random.randint(0,255)
	rcolors[i] = ('#%02X%02X%02X' % (r(),r(),r()))
print rcolors

# Create the Plot
from bokeh.plotting import *
from bokeh.models.glyphs import Patches
from bokeh.models import HoverTool

output_file("longhurst.html")

#bk.hold()

TOOLS="pan,wheel_zoom,box_zoom,hover,reset,previewsave"
f=figure(title="Longhurst regions", tools=TOOLS, plot_width=900, plot_height=800)

for region in regions:
    data = getDict(region, dat)
    f.patches(data[region]['lat_list'], data[region]['lng_list'],fill_color=rcolors[region], line_color='#000000')

hots_pcr=(27.22, -158)
f.circle(hots_pcr)

hover = f.select(dict(type=HoverTool))
hover.snap_to_data = False
hover.tooltips = [
    # add to this
    ("index", "$index"),
    ("(x,y)", "($x, $y)"),
    ("region", "@region"),
    ("fill color", "$color[hex, swatch]:fill_color"),
    ("foo", "@foo"),
    ("bar", "@bar"),
]

show(f)