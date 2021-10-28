import geopandas as gpd
from momepy.elements import _queen_corners

tess = gpd.read_file('files/prg.gpkg', layer='tessallation')

sindex = tess.sindex

tess = _queen_corners(tess, 2, sindex)

tess.to_file('files/prg.gpkg', layer='queen', driver='GPKG')
