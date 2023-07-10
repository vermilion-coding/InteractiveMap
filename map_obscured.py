import os
import webbrowser
import sys
import folium
from folium.plugins import FloatImage
import earthpy as et
from PIL import Image
import io, base64

sys.path.insert(0, '..')

# Adds images
# region
# 450 Image
path = r'imgs/map1 blurry.jpg'
fourfifty = Image.open(path).convert('RGBA')

# 414 Image
path2 = r'imgs/map2 blurry.jpg'
fourfourteen = Image.open(path2).convert('RGBA')

# 441 Image
path3 = r'imgs/map3 blurry.jpg'
fourfortyone = Image.open(path3).convert('RGBA')

# 470 Image
path4 = r'imgs/map4 blurry.jpg'
fourseventy = Image.open(path4).convert('RGBA')

# 423 Image
path5 = r'imgs/map5 blurry.jpg'
fourtwentythree = Image.open(path5).convert('RGBA')

# 137 Image
path6 = r'imgs/map6 blurry.jpg'
one = Image.open(path6).convert('RGBA')
# endregion

# Pulls data from map repository
data = et.data.get_data('colorado-flood')

os.chdir(os.path.join(et.io.HOME, 'earth-analytics', 'data'))

# Map initialization
m = folium.Map(location=[36.428472, -82.298992], zoom_start=16.2, max_bounds=True)

# Adds legend
# region
markerformat = """<br> &nbsp; {item} 
                <i class="fa-sharp fa-solid fa-location-pin fa-xl" 
                style="color:{col}"></i>"""
iconformat = """<br> &nbsp; {item} &nbsp; <i class="fa fa-p"></i>"""
firstfloor = markerformat.format(item="First Floor:", col="black")
secondfloor = markerformat.format(item="Second Floor:", col="red")
printer = iconformat.format(item="Printer =")

legend_html = """
     <div style="
     position: fixed; 
     bottom: 50px; left: 50px; width: 195px; height: 200px; 
     border:4px solid grey; z-index:9999; 

     background-color:white;
     opacity: .85;
     font-size:14px;
     font-weight: bold;

     ">

     <center> <font size="3"> <u>{title}</u> </font> </center> 

     {itm_txt}

      </div> """.format(title="Legend", itm_txt=firstfloor + secondfloor + printer)
m.get_root().html.add_child(folium.Element(legend_html))
# endregion

# Marker creation
# region
# 450 Markers
folium.Marker(
    location=[36.4334, -82.2949477191261],
    draggable=True,
    popup='<h4> <b>--- -----</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-thin fa-p', color='black')
).add_to(m)

folium.Marker(
    location=[36.43361961833127, -82.2949477191261],
    draggable=True,
    popup='<h4> <b>--- ---- -----</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

folium.Marker(
    location=[36.43275, -82.29378],
    draggable=True,
    popup='<h4> <b>--- -------- ------</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

folium.Marker(
    location=[36.43245, -82.29585],
    draggable=True,
    popup='<h4> <b>--- --------</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

folium.Marker(
    location=[36.43377, -82.2944],
    draggable=True,
    popup='<h4> <b>--- --</b> </h4>' + 'ID:------',
    icon=folium.Icon(color='red', icon='fa-solid fa-p')
).add_to(m)

corporate = folium.Marker(
    location=[36.43361961833127, -82.2951],
    draggable=True,
    popup='<h4> <b>--- ---- ----</b> </h4>' + 'ID:------',
    icon=folium.Icon(color='red', icon='fa-solid fa-p')
).add_to(m)

folium.Marker(
    location=[36.43345, -82.29554],
    draggable=True,
    popup='<h4> <b>--- ---</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-thin fa-p', color='black')
).add_to(m)

folium.Marker(
    location=[36.43355, -82.29424],
    draggable=True,
    popup='<h4> <b>--- -------- ---------</b> </h4>' + 'ID:------',
    icon=folium.Icon(color='red', icon='fa-solid fa-p')
).add_to(m)

folium.Marker(
    location=[36.43328, -82.29561],
    draggable=True,
    popup='<h4> <b>--- -------</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-thin fa-p', color='red')
).add_to(m)

folium.Marker(
    location=[36.43328, -82.2955],
    draggable=True,
    popup='<h4> <b>--- --- ------</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-thin fa-p', color='black')
).add_to(m)

folium.Marker(
    location=[36.43284, -82.2954],
    draggable=True,
    popup='<h4> <b>--- --- ------</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

folium.Marker(
    location=[36.431691, -82.295226],
    draggable=True,
    popup='<h4> <b>--- ----- ----</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

# 414 Markers

folium.Marker(
    location=[36.4318, -82.2963],
    draggable=True,
    popup='<h4> <b>--- ------- ------ --------</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='red')
).add_to(m)

folium.Marker(
    location=[36.4310, -82.2958],
    draggable=True,
    popup='<h4> <b>--- ----------- ------ --</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

folium.Marker(
    location=[36.4308, -82.29648],
    draggable=True,
    popup='<h4> <b>--- ----------- -------</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

folium.Marker(
    location=[36.4307, -82.29631],
    draggable=True,
    popup='<h4> <b>--- -------- ------</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

folium.Marker(
    location=[36.43108, -82.29735],
    draggable=True,
    popup='<h4> <b>--- ----- ----</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

folium.Marker(
    location=[36.43035, -82.298],
    draggable=True,
    popup='<h4> <b>--- ----- ------- ------</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

folium.Marker(
    location=[36.43035, -82.297],
    draggable=True,
    popup='<h4> <b>--- ----------- ------ --</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

folium.Marker(
    location=[36.4301, -82.2975],
    draggable=True,
    popup='<h4> <b>--- ----------- ------ --</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

# 441

folium.Marker(
    location=[36.43355, -82.3002],
    draggable=True,
    popup='<h4> <b>--- ----- ---- ----</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

folium.Marker(
    location=[36.4334, -82.3004],
    draggable=True,
    popup='<h4> <b>--- --------- ----------</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

folium.Marker(
    location=[36.4334, -82.30015],
    draggable=True,
    popup='<h4> <b>--- ----- ---- -----</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

folium.Marker(
    location=[36.4339, -82.2994],
    draggable=True,
    popup='<h4> <b>--- ------- ----</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

folium.Marker(
    location=[36.43405, -82.29908],
    draggable=True,
    popup='<h4> <b>--- ------- -----</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

folium.Marker(
    location=[36.4342, -82.2989],
    draggable=True,
    popup='<h4> <b>--- ---------- ----</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

folium.Marker(
    location=[36.4342, -82.29908],
    draggable=True,
    popup='<h4> <b>--- ---------- ------</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

# 470


folium.Marker(
    location=[36.433771, -82.293445],
    draggable=True,
    popup='<h4> <b>--- ---- -----</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

folium.Marker(
    location=[36.434129, -82.293429],
    draggable=True,
    popup='<h4> <b>--- ---- -------</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

folium.Marker(
    location=[36.433594, -82.292426],
    draggable=True,
    popup='<h4> <b>--- --- ------</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

# 423

folium.Marker(
    location=[36.422583, -82.305230],
    draggable=True,
    popup='<h4> <b>--- -------- ------</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

folium.Marker(
    location=[36.422519, -82.305252],
    draggable=True,
    popup='<h4> <b>--- -------- -----</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

folium.Marker(
    location=[36.423835, -82.303750],
    draggable=True,
    popup='<h4> <b>--- ----------</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

folium.Marker(
    location=[36.423827, -82.303659],
    draggable=True,
    popup='<h4> <b>--- ---------- -</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

folium.Marker(
    location=[36.430599, -82.308476],
    draggable=True,
    popup='<h4> <b>--- --- --------- ------</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

folium.Marker(
    location=[36.430702, -82.308632],
    draggable=True,
    popup='<h4> <b>--- --- -------</b> </h4>' + 'ID:------',
    icon=folium.Icon(icon='fa-solid fa-p', color='black')
).add_to(m)

# endregion

# Overlays the floor plan image on top of the interactive map
# Adds that image overlay to the map
# region
# 450
for r in [60]:
    b = io.BytesIO()
    fourfifty.rotate(r, fillcolor=0, expand=True).save(b, format='PNG')
    b64 = base64.b64encode(b.getvalue())
    folium.raster_layers.ImageOverlay(
        image=f'data:image/png;base64,{b64.decode("utf-8")}',
        name=f'450',
        bounds=[[36.43420744071162, -82.29621528761145], [36.43139475002618, -82.29281856494431]],
        opacity=1,
        interactive=False,
        cross_origin=False,
        zindex=1,
    ).add_to(m)

# 414
for r in [230]:
    b = io.BytesIO()
    fourfourteen.rotate(r, fillcolor=0, expand=True).save(b, format='PNG')
    b64 = base64.b64encode(b.getvalue())
    folium.raster_layers.ImageOverlay(
        image=f'data:image/png;base64,{b64.decode("utf-8")}',
        name=f'414',
        bounds=[[36.429409817808676, -82.29826529067668], [36.43191971586276, -82.29512662398389]],
        opacity=1,
        interactive=False,
        cross_origin=False,
        zindex=1,
    ).add_to(m)

# 441
for r in [380]:
    b = io.BytesIO()
    fourfortyone.rotate(r, fillcolor=0, expand=True).save(b, format='PNG')
    b64 = base64.b64encode(b.getvalue())
    folium.raster_layers.ImageOverlay(
        image=f'data:image/png;base64,{b64.decode("utf-8")}',
        name=f'441',
        bounds=[[36.43323148021702, -82.30070521343065], [36.43473341268421, -82.29742218972082]],
        opacity=1,
        interactive=False,
        cross_origin=False,
        zindex=1,
    ).add_to(m)

# 470
for r in [0]:
    b = io.BytesIO()
    fourseventy.rotate(r, fillcolor=0, expand=True).save(b, format='PNG')
    b64 = base64.b64encode(b.getvalue())
    folium.raster_layers.ImageOverlay(
        image=f'data:image/png;base64,{b64.decode("utf-8")}',
        name=f'450',
        bounds=[[36.433495, -82.291707], [36.434690, -82.293525]],
        opacity=1,
        interactive=False,
        cross_origin=False,
        zindex=1,
    ).add_to(m)

# 423
for r in [260]:
    b = io.BytesIO()
    fourtwentythree.rotate(r, fillcolor=0, expand=True).save(b, format='PNG')
    b64 = base64.b64encode(b.getvalue())
    folium.raster_layers.ImageOverlay(
        image=f'data:image/png;base64,{b64.decode("utf-8")}',
        name=f'450',
        bounds=[[36.422296, -82.303251], [36.424142, -82.305402]],
        opacity=1,
        interactive=False,
        cross_origin=False,
        zindex=1,
    ).add_to(m)

# 137-157
for r in [360]:
    b = io.BytesIO()
    one.rotate(r, fillcolor=0, expand=True).save(b, format='PNG')
    b64 = base64.b64encode(b.getvalue())
    folium.raster_layers.ImageOverlay(
        image=f'data:image/png;base64,{b64.decode("utf-8")}',
        name=f'450',
        bounds=[[36.430357, -82.309291], [36.431553, -82.307634]],
        opacity=1,
        interactive=False,
        cross_origin=False,
        zindex=1,
    ).add_to(m)
# endregion

# Adds coordinates on click
popup1 = folium.ClickForLatLng(alert=False)
m.add_child(popup1)

# Copies clicked coordinates to clipboard
popup2 = folium.LatLngPopup()
m.add_child(popup2)

m.fit_bounds([36.436033, -82.298069], [36.421686, -82.299099])

# Adds Title
loc = '---- ----- -----: Asset Locator'
title_html = '''
             <h3 align="center" style="font-size:24px"><b>{}</b></h3>
             '''.format(loc)
m.get_root().html.add_child(folium.Element(title_html))

folium.LayerControl().add_to(m)

# Saves the map as an HTML file then opens it in a browser
m.save("map.html")
webbrowser.open("map.html")
