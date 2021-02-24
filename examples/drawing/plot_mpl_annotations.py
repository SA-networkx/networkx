"""
=================
Custom node icons
=================

Example of using custom icons to represent nodes with matplotlib.
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import networkx as nx

# Image URLs for graph nodes
icon_urls = {
    "router": "https://www.materialui.co/materialIcons/hardware/router_black_144x144.png",
    "switch": "https://www.materialui.co/materialIcons/action/dns_black_144x144.png",
    "PC": "https://www.materialui.co/materialIcons/hardware/computer_black_144x144.png",
}

# Load images from web
images = {k: mpimg.imread(url) for k, url in icon_urls.items()}

# Generate the computer network graph
G = nx.Graph()

G.add_node("router", image=images["router"])
for i in range(1, 4):
    G.add_node(f"switch_{i}", image=images["switch"])
    for j in range(1, 4):
        G.add_node("PC_" + str(i) + "_" + str(j), image=images["PC"])

G.add_edge("router", "switch_1")
G.add_edge("router", "switch_2")
G.add_edge("router", "switch_3")
for u in range(1, 4):
    for v in range(1, 4):
        G.add_edge("switch_" + str(u), "PC_" + str(u) + "_" + str(v))

# get layout and draw edges
pos = nx.spring_layout(G)
fig, ax = plt.subplots()
nx.draw_networkx_edges(G, pos=pos, ax=ax)

# Get the coordinate system for the whole plot (scaled between xlim and ylim). Then take the Transform.
tr_figure = ax.transData.transform
# Get the coordinate system for the whole plot (scaled between 0 and 1). Then take the Transform.
tr_axes = fig.transFigure.inverted().transform

# Select the size of the image (relative to the X axis)
icon_size = (ax.get_xlim()[1] - ax.get_xlim()[0]) * 0.025
icon_center = icon_size / 2.0

# Add the respective image to each node
for n in G.nodes:
    xf, yf = tr_figure(pos[n])
    xa, ya = tr_axes((xf, yf))
    # get overlapped axes and plot icon
    a = plt.axes([xa - icon_center, ya - icon_center, icon_size, icon_size])
    a.imshow(G.nodes[n]["image"])
    a.axis("off")
plt.show()
